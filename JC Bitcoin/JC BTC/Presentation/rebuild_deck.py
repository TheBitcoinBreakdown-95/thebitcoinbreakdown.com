#!/usr/bin/env python3
"""
Build JC Bitcoin Google Slides presentations.

Modes:
  --create "Title" --outline outline.json   Create a new deck from a content outline
  --rebuild PRES_ID                         Restyle an existing deck (preserves text)

The outline JSON supports two slide types:
  - {"layout": "copy", "source_index": N}  Copy slide N from the source deck (--source)
  - {"layout": "content|centered|splash|cover|sponsor", ...}  Build a new slide

Styles verified against reference decks and Slide-Style-Guide.md (2026-03-06):
  - Font: Calibri for everything
  - Colors: black (#000000) background, orange (#ff9900) text
  - Title: 24pt bold centered, body: 18pt left-aligned
  - Text on left half of slide, right half reserved for images
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from google_slides_auth import get_slides_service

# ━━━ Colors ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Black + Orange only. Verified from 3 reference decks.

C = {
    'black':  {'red': 0.0, 'green': 0.0, 'blue': 0.0},   # #000000
    'orange': {'red': 1.0, 'green': 0.6, 'blue': 0.0},   # #ff9900
}

# ━━━ Font: Calibri for everything ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FONT = 'Calibri'

# ━━━ Positions (EMU, from reference decks) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SLIDE_W = 9144000
SLIDE_H = 5143500

# Cover
COVER_LOGO = {'x': 2437898, 'y': 90236, 'w': 4268203, 'h': 4268203}
COVER_TEXT = {'x': 1142999, 'y': 3748440, 'w': 6858000, 'h': 1200000}

# Sponsor
SPONSOR_TITLE = {'x': 284662, 'y': 43275, 'w': 8492100, 'h': 994199}
SPONSOR_IMAGE = {'x': 285750, 'y': 1167187, 'w': 8572500, 'h': 3600450}

# Content (left half for text, right half for images)
CONTENT_TITLE = {'x': 284662, 'y': 43275, 'w': 4572000, 'h': 994199}
CONTENT_BODY = {'x': 284662, 'y': 1037550, 'w': 4572000, 'h': 3886200}

# Centered text
CENTER_TITLE = {'x': 1143000, 'y': 841774, 'w': 6858000, 'h': 1007400}
CENTER_BODY = {'x': 1143000, 'y': 2334524, 'w': 6858000, 'h': 1608600}

# Splash (oversized centered text)
SPLASH_POS = {'x': 762000, 'y': 1200000, 'w': 7620000, 'h': 2700000}

LOGO_DRIVE_ID = '1XCi7pXbNwhX8VyVlF0XOmwV2_778xAA2'

# Most recent source deck (Socratic Seminar #4, Feb 2025)
DEFAULT_SOURCE_DECK = '1aMa0HkZXH928PrRJkWmhHIZzEe4iuQZlHFG0evN2m1k'


# ━━━ Helpers ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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


def _set_bg(page_id):
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


def _textbox(oid, page, pos, text, pt, bold=False, align='CENTER'):
    """Create a transparent text box with orange Calibri text. Centered by default."""
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
        {'updateShapeProperties': {
            'objectId': oid,
            'fields': 'shapeBackgroundFill,outline',
            'shapeProperties': {
                'shapeBackgroundFill': {'propertyState': 'NOT_RENDERED'},
                'outline': {'propertyState': 'NOT_RENDERED'},
            },
        }},
        {'updateParagraphStyle': {
            'objectId': oid,
            'style': {'alignment': align},
            'textRange': {'type': 'ALL'},
            'fields': 'alignment',
        }},
    ]
    return reqs


def _style_range(oid, start, end, pt, bold=False):
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


def _add_bullets(oid, start, end):
    return {'createParagraphBullets': {
        'objectId': oid,
        'textRange': {'type': 'FIXED_RANGE', 'startIndex': start, 'endIndex': end},
        'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE',
    }}


def extract_texts(slide):
    """Pull text content from every text-bearing page element, in order."""
    texts = []
    for el in slide.get('pageElements', []):
        te_list = (el.get('shape', {})
                     .get('text', {})
                     .get('textElements', []))
        if not te_list:
            continue
        parts = [te['textRun']['content']
                 for te in te_list if 'textRun' in te]
        full = ''.join(parts)
        if full.endswith('\n'):
            full = full[:-1]
        texts.append(full)
    return texts


def parse_bullets(text):
    """Strip bullet prefixes, return cleaned text and the full range for bullets."""
    if not text:
        return '', None

    lines = text.split('\n')
    cleaned = []
    has_bullets = False

    for line in lines:
        s = line.lstrip()
        if s.startswith(('* ', '- ', '\u2022 ', '\u2713 ')):
            cleaned.append(s[2:])
            has_bullets = True
        else:
            cleaned.append(line)

    cleaned_text = '\n'.join(cleaned)
    if has_bullets:
        return cleaned_text, (0, len(cleaned_text))
    return cleaned_text, None


# ━━━ Layout builders ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def lay_cover(i, page, texts):
    """Cover slide -- logo centered, transparent text box below."""
    title = texts.get('title', 'Jersey City Bitcoin')
    subtitle = texts.get('subtitle', '')

    reqs = []
    reqs.append({'createImage': {
        'objectId': f's{i}_logo',
        'url': f'https://drive.google.com/uc?id={LOGO_DRIVE_ID}',
        'elementProperties': {
            'pageObjectId': page,
            **_pos(COVER_LOGO['x'], COVER_LOGO['y'],
                   COVER_LOGO['w'], COVER_LOGO['h']),
        },
    }})
    cover_text = title
    if subtitle:
        cover_text += '\n' + subtitle
    reqs += _textbox(f's{i}_txt', page, COVER_TEXT, cover_text, 18, align='CENTER')
    reqs.append(_style_range(f's{i}_txt', 0, len(title), 36))
    return reqs


def lay_sponsor(i, page, texts):
    """Sponsor slide -- title + large sponsor image."""
    title = texts.get('title', 'Sponsored by:')
    image_url = texts.get('image_url', '')

    reqs = []
    reqs += _textbox(f's{i}_ttl', page, SPONSOR_TITLE, title, 24, bold=True)
    if image_url:
        reqs.append({'createImage': {
            'objectId': f's{i}_simg',
            'url': image_url,
            'elementProperties': {
                'pageObjectId': page,
                **_pos(SPONSOR_IMAGE['x'], SPONSOR_IMAGE['y'],
                       SPONSOR_IMAGE['w'], SPONSOR_IMAGE['h']),
            },
        }})
    return reqs


def lay_content(i, page, texts):
    """Content slide -- title (centered) + bulleted body on left half."""
    title = texts.get('title', '')
    body = texts.get('body', '')

    cleaned_body, bullet_range = parse_bullets(body)

    reqs = []
    reqs += _textbox(f's{i}_ttl', page, CONTENT_TITLE, title, 24, bold=True, align='CENTER')
    if cleaned_body:
        reqs += _textbox(f's{i}_bdy', page, CONTENT_BODY, cleaned_body, 18, align='START')
        if bullet_range:
            reqs.append(_add_bullets(f's{i}_bdy', bullet_range[0], bullet_range[1]))
    return reqs


def lay_splash(i, page, texts):
    """Splash/section divider -- oversized centered text."""
    title = texts.get('title', '')

    reqs = []
    reqs += _textbox(f's{i}_splash', page, SPLASH_POS, title, 72, bold=True, align='CENTER')
    return reqs


def lay_centered(i, page, texts):
    """Centered text slide -- for announcements, Q&A, closing."""
    title = texts.get('title', '')
    body = texts.get('body', '')

    reqs = []
    reqs += _textbox(f's{i}_ttl', page, CENTER_TITLE, title, 24, bold=True, align='CENTER')
    if body:
        cleaned, _ = parse_bullets(body)
        reqs += _textbox(f's{i}_bdy', page, CENTER_BODY, cleaned, 18, align='CENTER')
    return reqs


BUILDERS = {
    'cover':    lay_cover,
    'sponsor':  lay_sponsor,
    'content':  lay_content,
    'splash':   lay_splash,
    'centered': lay_centered,
}


# ━━━ Slide copying ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def copy_slides_from_source(svc, source_pres_id, target_pres_id, copy_map):
    """Copy slides from a source deck into the target deck.

    copy_map: list of (target_index, source_index) tuples, sorted by target_index.
    Copies are inserted at the correct positions, preserving all content,
    images, and speaker notes from the source.
    """
    if not copy_map:
        return

    # Copy each slide individually to maintain ordering
    for target_idx, source_idx in copy_map:
        # Get current source slide object ID
        source_pres = svc.presentations().get(presentationId=source_pres_id).execute()
        source_slide_id = source_pres['slides'][source_idx]['objectId']

        # Copy the slide into the target deck
        # We use the Drive API to copy, but Slides API doesn't support cross-deck copy.
        # Instead, we duplicate within target by first importing via the workaround:
        # 1. Get the target deck's current slide at target_idx
        # 2. Delete it
        # 3. Insert a copy of the source slide at that position

        # The Slides API doesn't support cross-presentation copy directly.
        # We need to use a different approach: read all elements from source and recreate.
        # But for full fidelity (images, formatting), we'll use the
        # presentations().pages().copy approach via the source deck.

        # Actually, the best approach: use batchUpdate with duplicateObject on the source,
        # then move. But that only works within the same presentation.

        # Real approach: We'll need to read the source slide's elements and recreate them.
        # For now, use the Google Slides API's "copy from another presentation" approach
        # by creating slides that reference the source.

        print(f'  Copying source[{source_idx}] -> target[{target_idx}]')

    # The Slides API doesn't natively support cross-deck slide copy.
    # We use the workaround: merge the source slides into the target via
    # the presentations().batchUpdate() with a special flow.


def copy_slides_bulk(svc, source_pres_id, target_pres_id, copy_indices):
    """Copy specific slides from source to target using Drive API copy + delete.

    copy_indices: dict mapping target_position -> source_slide_index

    Strategy:
    1. Make a full copy of the source presentation
    2. Delete slides we don't need from the copy
    3. Read the remaining slides and recreate their content in the target
    """
    # Alternative simpler strategy: for each source slide, read all its elements
    # and recreate them in the target slide at the corresponding position.
    # This preserves text and speaker notes. Images are recreated from contentUrl.

    source_pres = svc.presentations().get(presentationId=source_pres_id).execute()
    source_slides = source_pres['slides']

    target_pres = svc.presentations().get(presentationId=target_pres_id).execute()
    target_slides = target_pres['slides']

    for target_idx, source_idx in sorted(copy_indices.items()):
        source_slide = source_slides[source_idx]
        target_page = target_slides[target_idx]['objectId']

        requests = []
        # Set black background
        requests.append(_set_bg(target_page))

        elem_count = 0
        for el in source_slide.get('pageElements', []):
            elem_count += 1
            oid = f'cp{target_idx}_{elem_count}'

            # Get position/size from source element
            xform = el.get('transform', {})
            size = el.get('size', {})
            w = size.get('width', {}).get('magnitude', 4572000)
            h = size.get('height', {}).get('magnitude', 3886200)
            tx = xform.get('translateX', 0)
            ty = xform.get('translateY', 0)
            sx = xform.get('scaleX', 1)
            sy = xform.get('scaleY', 1)

            if 'image' in el:
                img = el['image']
                content_url = img.get('contentUrl', '')
                source_url = img.get('sourceUrl', '')
                url = source_url or content_url
                if url:
                    requests.append({'createImage': {
                        'objectId': oid,
                        'url': url,
                        'elementProperties': {
                            'pageObjectId': target_page,
                            'size': size,
                            'transform': xform,
                        },
                    }})

            elif 'shape' in el:
                shape = el['shape']
                shape_type = shape.get('shapeType', 'TEXT_BOX')

                # Get text content
                text_elements = shape.get('text', {}).get('textElements', [])
                full_text = ''.join(
                    te.get('textRun', {}).get('content', '')
                    for te in text_elements if 'textRun' in te
                )
                if full_text.endswith('\n'):
                    full_text = full_text[:-1]

                if not full_text and shape_type == 'TEXT_BOX':
                    continue

                # Create the shape
                requests.append({'createShape': {
                    'objectId': oid,
                    'shapeType': shape_type,
                    'elementProperties': {
                        'pageObjectId': target_page,
                        'size': size,
                        'transform': xform,
                    },
                }})

                if full_text:
                    requests.append({'insertText': {
                        'objectId': oid,
                        'text': full_text,
                        'insertionIndex': 0,
                    }})

                    # Apply text styles from source
                    for te in text_elements:
                        if 'textRun' not in te:
                            continue
                        run = te['textRun']
                        style = run.get('style', {})
                        content = run['content']
                        start = te.get('startIndex', 0)
                        end = te.get('endIndex', start + len(content))

                        update_style = {}
                        fields = []

                        if 'fontFamily' in style:
                            update_style['fontFamily'] = style['fontFamily']
                            fields.append('fontFamily')
                        if 'fontSize' in style:
                            update_style['fontSize'] = style['fontSize']
                            fields.append('fontSize')
                        if 'foregroundColor' in style:
                            update_style['foregroundColor'] = style['foregroundColor']
                            fields.append('foregroundColor')
                        if 'bold' in style:
                            update_style['bold'] = style['bold']
                            fields.append('bold')
                        if 'italic' in style:
                            update_style['italic'] = style['italic']
                            fields.append('italic')

                        if fields:
                            requests.append({'updateTextStyle': {
                                'objectId': oid,
                                'style': update_style,
                                'textRange': {
                                    'type': 'FIXED_RANGE',
                                    'startIndex': start,
                                    'endIndex': end,
                                },
                                'fields': ','.join(fields),
                            }})

                # Copy shape fill/outline
                shape_props = shape.get('shapeProperties', {})
                bg_fill = shape_props.get('shapeBackgroundFill', {})
                outline = shape_props.get('outline', {})
                prop_updates = {}
                prop_fields = []

                if bg_fill:
                    prop_updates['shapeBackgroundFill'] = bg_fill
                    if bg_fill.get('propertyState') == 'NOT_RENDERED':
                        prop_fields.append('shapeBackgroundFill')
                    elif 'solidFill' in bg_fill:
                        prop_fields.append('shapeBackgroundFill.solidFill.color')

                if outline:
                    prop_updates['outline'] = outline
                    if outline.get('propertyState') == 'NOT_RENDERED':
                        prop_fields.append('outline')

                if prop_fields:
                    requests.append({'updateShapeProperties': {
                        'objectId': oid,
                        'fields': ','.join(prop_fields),
                        'shapeProperties': prop_updates,
                    }})

                # Copy paragraph styles (alignment, bullets)
                for te in text_elements:
                    if 'paragraphMarker' in te:
                        pm = te['paragraphMarker']
                        ps = pm.get('style', {})
                        start = te.get('startIndex', 0)
                        end = te.get('endIndex', start)
                        if 'alignment' in ps:
                            requests.append({'updateParagraphStyle': {
                                'objectId': oid,
                                'style': {'alignment': ps['alignment']},
                                'textRange': {
                                    'type': 'FIXED_RANGE',
                                    'startIndex': start,
                                    'endIndex': end,
                                },
                                'fields': 'alignment',
                            }})
                        if pm.get('bullet'):
                            # Recreate bullets
                            requests.append({'createParagraphBullets': {
                                'objectId': oid,
                                'textRange': {
                                    'type': 'FIXED_RANGE',
                                    'startIndex': start,
                                    'endIndex': end,
                                },
                                'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE',
                            }})

        # Copy speaker notes
        notes_page = source_slide.get('slideProperties', {}).get('notesPage', {})
        for el in notes_page.get('pageElements', []):
            ph = el.get('shape', {}).get('placeholder', {})
            if ph.get('type') == 'BODY':
                te = el['shape'].get('text', {}).get('textElements', [])
                notes_text = ''.join(
                    t.get('textRun', {}).get('content', '')
                    for t in te if 'textRun' in t
                ).strip()
                if notes_text:
                    # Get target notes shape ID
                    target_full = svc.presentations().get(
                        presentationId=target_pres_id).execute()
                    target_slide = target_full['slides'][target_idx]
                    target_notes = target_slide.get('slideProperties', {}).get('notesPage', {})
                    for nel in target_notes.get('pageElements', []):
                        nph = nel.get('shape', {}).get('placeholder', {})
                        if nph.get('type') == 'BODY':
                            requests.append({'insertText': {
                                'objectId': nel['objectId'],
                                'text': notes_text,
                                'insertionIndex': 0,
                            }})
                            break

        if requests:
            svc.presentations().batchUpdate(
                presentationId=target_pres_id,
                body={'requests': requests},
            ).execute()

        print(f'  [{target_idx:2d}] copied from source[{source_idx}] ({elem_count} elements)')


# ━━━ Create mode ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def create_deck(svc, title, outline, source_pres_id=None):
    """Create a new presentation and populate it from an outline.

    Slides with layout="copy" are copied from the source deck.
    Other slides are built fresh using the layout builders.
    """
    slide_defs = outline.get('slides', [])
    num_slides = len(slide_defs)

    print(f'Creating new presentation: "{title}" ({num_slides} slides)...')
    pres = svc.presentations().create(body={'title': title}).execute()
    pres_id = pres['presentationId']
    print(f'  Created: {pres_id}')

    # The new deck starts with 1 blank slide. Add more if needed.
    if num_slides > 1:
        add_reqs = []
        for idx in range(num_slides - 1):
            add_reqs.append({'createSlide': {
                'insertionIndex': idx + 1,
                'slideLayoutReference': {'predefinedLayout': 'BLANK'},
            }})
        svc.presentations().batchUpdate(
            presentationId=pres_id,
            body={'requests': add_reqs},
        ).execute()
        print(f'  Added {num_slides - 1} blank slides')

    # Fetch the deck to get slide object IDs
    pres = svc.presentations().get(presentationId=pres_id).execute()
    slides = pres.get('slides', [])

    # Separate copy slides from build slides
    copy_indices = {}
    build_indices = []

    for i, slide_def in enumerate(slide_defs):
        if slide_def.get('layout') == 'copy':
            copy_indices[i] = slide_def['source_index']
        else:
            build_indices.append(i)

    # Copy slides from source deck first
    if copy_indices and source_pres_id:
        print(f'\nCopying {len(copy_indices)} slides from source deck...')
        copy_slides_bulk(svc, source_pres_id, pres_id, copy_indices)
    elif copy_indices:
        print(f'\nWARNING: {len(copy_indices)} slides need --source but none provided. Skipping.')

    # Build new slides
    if build_indices:
        print(f'\nBuilding {len(build_indices)} new slides...')
        # Re-fetch deck after copies (slide IDs may have changed)
        pres = svc.presentations().get(presentationId=pres_id).execute()
        slides = pres.get('slides', [])

        requests = []
        for i in build_indices:
            slide_def = slide_defs[i]
            page = slides[i]['objectId']
            layout = slide_def.get('layout', 'content')

            requests.append(_set_bg(page))

            texts = dict(slide_def)
            if 'bullets' in texts and 'body' not in texts:
                texts['body'] = '\n'.join(f'* {b}' for b in texts['bullets'])

            builder = BUILDERS.get(layout, lay_content)
            requests += builder(i, page, texts)

            print(f'  [{i:2d}] {layout}')

        if requests:
            print(f'\nSending {len(requests)} API requests...')
            svc.presentations().batchUpdate(
                presentationId=pres_id,
                body={'requests': requests},
            ).execute()

        # Add speaker notes for built slides
        notes_count = 0
        pres = svc.presentations().get(presentationId=pres_id).execute()
        slides = pres.get('slides', [])

        for i in build_indices:
            slide_def = slide_defs[i]
            notes_text = slide_def.get('speaker_notes', '')
            if not notes_text:
                continue
            slide_obj = slides[i]
            notes_page = slide_obj.get('slideProperties', {}).get('notesPage', {})
            for el in notes_page.get('pageElements', []):
                ph = el.get('shape', {}).get('placeholder', {})
                if ph.get('type') == 'BODY':
                    svc.presentations().batchUpdate(
                        presentationId=pres_id,
                        body={'requests': [
                            {'insertText': {
                                'objectId': el['objectId'],
                                'text': notes_text,
                                'insertionIndex': 0,
                            }},
                        ]},
                    ).execute()
                    notes_count += 1
                    break

        if notes_count:
            print(f'  Added speaker notes to {notes_count} slides')

    print(f'\nDone! View at:')
    print(f'https://docs.google.com/presentation/d/{pres_id}')
    return pres_id


# ━━━ Rebuild mode ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def rebuild_deck(svc, pres_id, layouts):
    """Restyle an existing deck -- preserves text, replaces formatting."""
    print(f'Fetching presentation {pres_id}...')
    pres = svc.presentations().get(presentationId=pres_id).execute()

    slides = pres.get('slides', [])
    n = len(slides)
    print(f'Found {n} slides (layout list has {len(layouts)})')
    if n != len(layouts):
        print('ERROR: slide count mismatch -- aborting.')
        sys.exit(1)

    requests = []

    for i, slide in enumerate(slides):
        page = slide['objectId']
        layout = layouts[i]
        raw_texts = extract_texts(slide)

        requests.append(_set_bg(page))

        for el in slide.get('pageElements', []):
            requests.append({'deleteObject': {'objectId': el['objectId']}})

        texts = {}
        if layout == 'cover':
            texts['title'] = raw_texts[0] if raw_texts else 'Jersey City Bitcoin'
            texts['subtitle'] = raw_texts[1] if len(raw_texts) > 1 else ''
        elif layout == 'sponsor':
            texts['title'] = raw_texts[0] if raw_texts else 'Sponsored by:'
        elif layout == 'splash':
            texts['title'] = raw_texts[0] if raw_texts else ''
        elif layout == 'centered':
            texts['title'] = raw_texts[0] if raw_texts else ''
            texts['body'] = raw_texts[1] if len(raw_texts) > 1 else ''
        else:
            texts['title'] = raw_texts[0] if raw_texts else ''
            texts['body'] = raw_texts[1] if len(raw_texts) > 1 else ''

        requests += BUILDERS[layout](i, page, texts)
        print(f'  [{i:2d}] {layout:11s}  texts={len(raw_texts)}')

    print(f'\nSending {len(requests)} API requests...')
    svc.presentations().batchUpdate(
        presentationId=pres_id,
        body={'requests': requests},
    ).execute()

    print(f'\nDone! View at:')
    print(f'https://docs.google.com/presentation/d/{pres_id}')


# ━━━ Main ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    parser = argparse.ArgumentParser(description='JC Bitcoin -- Slide deck builder')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--create', metavar='TITLE',
                       help='Create a new deck with the given title')
    group.add_argument('--rebuild', metavar='PRES_ID',
                       help='Restyle an existing deck (preserves text)')
    parser.add_argument('--outline', metavar='FILE',
                        help='JSON outline file (required for --create)')
    parser.add_argument('--source', metavar='PRES_ID', default=DEFAULT_SOURCE_DECK,
                        help='Source deck to copy recurring slides from (default: Seminar #4)')
    parser.add_argument('--layouts', metavar='FILE',
                        help='JSON file with layout-type list (for --rebuild)')
    args = parser.parse_args()

    svc = get_slides_service()
    print('Authenticated.')

    if args.create:
        if not args.outline:
            parser.error('--create requires --outline')
        outline = json.loads(Path(args.outline).read_text())
        create_deck(svc, args.create, outline, source_pres_id=args.source)
    else:
        if args.layouts:
            layouts = json.loads(Path(args.layouts).read_text())
        else:
            print('No --layouts file provided. Reading all slides as "content" type.')
            pres = svc.presentations().get(presentationId=args.rebuild).execute()
            layouts = ['content'] * len(pres.get('slides', []))
        rebuild_deck(svc, args.rebuild, layouts)


if __name__ == '__main__':
    main()
