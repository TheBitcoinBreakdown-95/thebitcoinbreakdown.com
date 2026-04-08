#!/usr/bin/env python3
"""
Add JC Bitcoin logos to a presentation deck.

- Cover slide (0): Main logo large and centered
- Slides 1+: Small icon/watermark bottom-right

Run AFTER rebuild_deck.py (which deletes all elements including logos).

Usage:
  python add_logos.py PRES_ID [--wide-logo DRIVE_ID] [--icon-logo DRIVE_ID]
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from google_slides_auth import get_slides_service

# Slide dimensions (standard 16:9)
SLIDE_W = 9144000
SLIDE_H = 5143500


def emu(v):
    return {'magnitude': v, 'unit': 'EMU'}


def create_image(obj_id, page_id, url, x, y, w, h):
    return {
        'createImage': {
            'objectId': obj_id,
            'url': url,
            'elementProperties': {
                'pageObjectId': page_id,
                'size': {
                    'width': emu(w),
                    'height': emu(h),
                },
                'transform': {
                    'scaleX': 1, 'scaleY': 1,
                    'translateX': x, 'translateY': y,
                    'unit': 'EMU',
                },
            },
        },
    }


def main():
    parser = argparse.ArgumentParser(description='Add JC Bitcoin logos to a deck')
    parser.add_argument('pres_id', help='Presentation ID')
    parser.add_argument('--wide-logo', metavar='DRIVE_ID',
                        help='Drive file ID of the wide/main logo')
    parser.add_argument('--icon-logo', metavar='DRIVE_ID',
                        help='Drive file ID of the small icon/mark logo')
    args = parser.parse_args()

    if not args.wide_logo and not args.icon_logo:
        print('ERROR: Provide at least one of --wide-logo or --icon-logo')
        sys.exit(1)

    svc = get_slides_service()
    print('Authenticated.')

    print(f'Fetching presentation {args.pres_id}...')
    pres = svc.presentations().get(presentationId=args.pres_id).execute()
    slides = pres.get('slides', [])
    print(f'Found {len(slides)} slides')

    requests = []

    # Cover slide (index 0): wide logo large and centered
    if args.wide_logo and slides:
        cover_page = slides[0]['objectId']
        logo_url = f'https://drive.google.com/uc?id={args.wide_logo}'
        logo_w = 5500000   # ~6 inches
        logo_h = 1800000   # ~2 inches
        logo_x = (SLIDE_W - logo_w) // 2
        logo_y = (SLIDE_H - logo_h) // 2
        requests.append(create_image(
            'logo_cover', cover_page, logo_url,
            logo_x, logo_y, logo_w, logo_h,
        ))
        print(f'  [0] Cover — wide logo centered')

    # Slides 1+: icon/watermark bottom-right
    if args.icon_logo and len(slides) > 1:
        icon_url = f'https://drive.google.com/uc?id={args.icon_logo}'
        icon_size = 360000   # ~0.4 inches
        icon_x = SLIDE_W - icon_size - 150000
        icon_y = SLIDE_H - icon_size - 150000
        for i in range(1, len(slides)):
            page_id = slides[i]['objectId']
            requests.append(create_image(
                f'logo_icon_{i}', page_id, icon_url,
                icon_x, icon_y, icon_size, icon_size,
            ))
        print(f'  [1-{len(slides)-1}] Icon logo bottom-right')

    if not requests:
        print('No logo requests to send.')
        return

    print(f'\nSending {len(requests)} requests...')
    resp = svc.presentations().batchUpdate(
        presentationId=args.pres_id,
        body={'requests': requests},
    ).execute()

    print(f'Done — {len(resp.get("replies", []))} replies.')
    print(f'\nhttps://docs.google.com/presentation/d/{args.pres_id}')


if __name__ == '__main__':
    main()
