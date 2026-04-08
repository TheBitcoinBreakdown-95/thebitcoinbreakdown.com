#!/usr/bin/env python3
"""Create a JC Bitcoin template deck matching the actual reference decks.

Verified against thumbnails from reference deck 1aMa0HkZXH928PrRJkWmhHIZzEe4iuQZlHFG0evN2m1k.
- Font: Calibri everywhere (theme-inherited, confirmed from master placeholders)
- Colors: black bg (#000000), orange text (#ff9900), nothing else
- Cover text box: transparent (NOT white — propertyState=NOT_RENDERED in reference)
- Title: ~36pt bold, body: 25-26pt, cover subtitle: 18pt
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from google_slides_auth import get_slides_service

# ── Colors ────────────────────────────────────────────────────────────────────
C = {
    'black':  {'red': 0.0, 'green': 0.0, 'blue': 0.0},   # #000000
    'orange': {'red': 1.0, 'green': 0.6, 'blue': 0.0},   # #ff9900
}

# ── Font: Calibri for everything (theme default in reference decks) ───────────
FONT = 'Calibri'

# ── Positions (EMU, measured from reference decks) ────────────────────────────
COVER_LOGO = {'x': 2437898, 'y': 90236, 'w': 4268203, 'h': 4268203}
COVER_TEXT = {'x': 1142999, 'y': 3748440, 'w': 6858000, 'h': 1200000}

CONTENT_TITLE = {'x': 284662, 'y': 43275, 'w': 8492100, 'h': 994199}
CONTENT_BODY = {'x': 284662, 'y': 1037550, 'w': 6944100, 'h': 3886200}

CENTER_TITLE = {'x': 1143000, 'y': 841774, 'w': 6858000, 'h': 1007400}
CENTER_BODY = {'x': 1143000, 'y': 2334524, 'w': 6858000, 'h': 1608600}

LOGO_DRIVE_ID = '1XCi7pXbNwhX8VyVlF0XOmwV2_778xAA2'


def emu(v):
    return {'magnitude': v, 'unit': 'EMU'}


def _pos(x, y, w, h):
    return {
        'size': {'width': emu(w), 'height': emu(h)},
        'transform': {
            'scaleX': 1, 'scaleY': 1,
            'translateX': x, 'translateY': y,
            'unit': 'EMU',
        },
    }


def set_bg(page_id):
    return {
        'updatePageProperties': {
            'objectId': page_id,
            'pageProperties': {
                'pageBackgroundFill': {
                    'solidFill': {'color': {'rgbColor': C['black']}},
                },
            },
            'fields': 'pageBackgroundFill.solidFill.color',
        },
    }


def textbox(oid, page, pos, text, pt, bold=False, align='START'):
    """Create a transparent text box with orange Calibri text."""
    reqs = [
        {'createShape': {
            'objectId': oid,
            'shapeType': 'TEXT_BOX',
            'elementProperties': {
                'pageObjectId': page,
                **_pos(pos['x'], pos['y'], pos['w'], pos['h']),
            },
        }},
        {'insertText': {
            'objectId': oid, 'text': text, 'insertionIndex': 0,
        }},
        {'updateTextStyle': {
            'objectId': oid,
            'style': {
                'fontFamily': FONT,
                'fontSize': {'magnitude': pt, 'unit': 'PT'},
                'foregroundColor': {'opaqueColor': {'rgbColor': C['orange']}},
                'bold': bold,
            },
            'textRange': {'type': 'ALL'},
            'fields': 'fontFamily,fontSize,foregroundColor,bold',
        }},
        # Transparent background, no outline
        {'updateShapeProperties': {
            'objectId': oid,
            'fields': 'shapeBackgroundFill,outline',
            'shapeProperties': {
                'shapeBackgroundFill': {'propertyState': 'NOT_RENDERED'},
                'outline': {'propertyState': 'NOT_RENDERED'},
            },
        }},
    ]
    if align != 'START':
        reqs.append({'updateParagraphStyle': {
            'objectId': oid,
            'style': {'alignment': align},
            'textRange': {'type': 'ALL'},
            'fields': 'alignment',
        }})
    return reqs


def style_range(oid, start, end, pt, bold=False):
    return {'updateTextStyle': {
        'objectId': oid,
        'style': {
            'fontFamily': FONT,
            'fontSize': {'magnitude': pt, 'unit': 'PT'},
            'foregroundColor': {'opaqueColor': {'rgbColor': C['orange']}},
            'bold': bold,
        },
        'textRange': {'type': 'FIXED_RANGE', 'startIndex': start, 'endIndex': end},
        'fields': 'fontFamily,fontSize,foregroundColor,bold',
    }}


def add_bullets(oid, start, end):
    return {'createParagraphBullets': {
        'objectId': oid,
        'textRange': {'type': 'FIXED_RANGE', 'startIndex': start, 'endIndex': end},
        'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE',
    }}


def main():
    svc = get_slides_service()
    print('Authenticated.')

    NUM_SLIDES = 7
    TITLE = 'JC Bitcoin - Template Deck'

    print(f'Creating "{TITLE}" ({NUM_SLIDES} slides)...')
    pres = svc.presentations().create(body={'title': TITLE}).execute()
    pres_id = pres['presentationId']
    print(f'  ID: {pres_id}')

    # Add extra blank slides
    add_reqs = [{'createSlide': {
        'insertionIndex': idx + 1,
        'slideLayoutReference': {'predefinedLayout': 'BLANK'},
    }} for idx in range(NUM_SLIDES - 1)]
    svc.presentations().batchUpdate(
        presentationId=pres_id, body={'requests': add_reqs},
    ).execute()

    pres = svc.presentations().get(presentationId=pres_id).execute()
    slides = pres['slides']
    reqs = []

    # ── Slide 0: Cover ────────────────────────────────────────────
    p = slides[0]['objectId']
    reqs.append(set_bg(p))
    reqs.append({'createImage': {
        'objectId': 'cover_logo',
        'url': f'https://drive.google.com/uc?id={LOGO_DRIVE_ID}',
        'elementProperties': {
            'pageObjectId': p,
            **_pos(COVER_LOGO['x'], COVER_LOGO['y'],
                   COVER_LOGO['w'], COVER_LOGO['h']),
        },
    }})
    # Transparent text box — orange text on black bg, no white fill
    cover_text = 'Jersey City Bitcoin Socratic Seminar #N'
    reqs += textbox('cover_txt', p, COVER_TEXT, cover_text, 18, align='CENTER')
    # Style "Jersey City Bitcoin" larger
    reqs.append(style_range('cover_txt', 0, len('Jersey City Bitcoin'), 36))
    print('  [0] cover')

    # ── Slide 1: Agenda ───────────────────────────────────────────
    p = slides[1]['objectId']
    reqs.append(set_bg(p))
    reqs += textbox('s1_ttl', p, CONTENT_TITLE, 'Agenda:', 36, bold=True)
    agenda = (
        'Welcome & Introductions\n'
        'Sponsor Acknowledgment\n'
        'Bitcoin News & Market Update\n'
        'Main Topic Discussion\n'
        'Lightning Round\n'
        'Q&A / Open Discussion\n'
        'Networking & Wrap-up'
    )
    reqs += textbox('s1_bdy', p, CONTENT_BODY, agenda, 26)
    reqs.append(add_bullets('s1_bdy', 0, len(agenda)))
    print('  [1] content - Agenda')

    # ── Slide 2: Guidelines ───────────────────────────────────────
    p = slides[2]['objectId']
    reqs.append(set_bg(p))
    reqs += textbox('s2_ttl', p, CONTENT_TITLE,
                    'JC Bitcoin Meetup General Guidelines', 36, bold=True)
    guidelines = (
        'Chatham House Rules apply\n'
        'No photos, videos, or public tagging without consent\n'
        'Bitcoin only - please limit discussion of other cryptocurrencies\n'
        'Not financial advice - educational only\n'
        'Respect the space'
    )
    reqs += textbox('s2_bdy', p, CONTENT_BODY, guidelines, 25)
    reqs.append(add_bullets('s2_bdy', 0, len(guidelines)))
    print('  [2] content - Guidelines')

    # ── Slide 3: Splash divider ───────────────────────────────────
    p = slides[3]['objectId']
    reqs.append(set_bg(p))
    splash_pos = {'x': 762000, 'y': 1200000, 'w': 7620000, 'h': 2700000}
    reqs += textbox('s3_splash', p, splash_pos,
                    'TOPIC\nGOES\nHERE', 72, bold=True, align='CENTER')
    print('  [3] splash divider')

    # ── Slide 4: Content topic ────────────────────────────────────
    p = slides[4]['objectId']
    reqs.append(set_bg(p))
    reqs += textbox('s4_ttl', p, CONTENT_TITLE,
                    'Content Slide Title:', 36, bold=True)
    topic = (
        'Key point about the topic\n'
        'Supporting detail or example\n'
        'Historical context or data\n'
        'Implications for Bitcoin users\n'
        'Action items or takeaways'
    )
    reqs += textbox('s4_bdy', p, CONTENT_BODY, topic, 26)
    reqs.append(add_bullets('s4_bdy', 0, len(topic)))
    print('  [4] content - Topic')

    # ── Slide 5: Full-text centered ───────────────────────────────
    p = slides[5]['objectId']
    reqs.append(set_bg(p))
    reqs += textbox('s5_ttl', p, CENTER_TITLE,
                    'Announcements', 36, bold=True, align='CENTER')
    announcements = (
        'Next meetup: Month DD, YYYY\n'
        'Follow us @JCBitcoin\n'
        'Join the mailing list at jcbitcoin.org'
    )
    reqs += textbox('s5_bdy', p, CENTER_BODY, announcements, 26, align='CENTER')
    print('  [5] centered - Announcements')

    # ── Slide 6: Q&A ─────────────────────────────────────────────
    p = slides[6]['objectId']
    reqs.append(set_bg(p))
    qa_pos = {'x': 1143000, 'y': 1500000, 'w': 6858000, 'h': 2000000}
    reqs += textbox('s6_qa', p, qa_pos, 'Questions?', 40, bold=True, align='CENTER')
    print('  [6] Q&A')

    # ── Send ──────────────────────────────────────────────────────
    print(f'\nSending {len(reqs)} API requests...')
    svc.presentations().batchUpdate(
        presentationId=pres_id, body={'requests': reqs},
    ).execute()

    url = f'https://docs.google.com/presentation/d/{pres_id}'
    print(f'\nDone! View at:\n{url}')
    return pres_id


if __name__ == '__main__':
    main()
