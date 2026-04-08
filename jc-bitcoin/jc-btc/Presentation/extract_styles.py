#!/usr/bin/env python3
"""Extract styles (colors, fonts, sizes, layouts) from existing JC Bitcoin presentations."""

import json
import sys
from collections import Counter
from pathlib import Path

# Add parent dir so we can import the auth module
sys.path.insert(0, str(Path(__file__).resolve().parent))
from google_slides_auth import get_slides_service

PRESENTATION_IDS = [
    '1aMa0HkZXH928PrRJkWmhHIZzEe4iuQZlHFG0evN2m1k',
    '16cCbevm-E4bFNvv4J_XHXfIo6JD-YsorjXtfoLrCNXQ',
    '1NzXPWR3A5ONu9kxXV8aWEqrtEkWz1CNIUwGv0KJITEA',
]

OUTPUT_FILE = Path(__file__).resolve().parent / 'extract_styles_output.json'


def rgb_to_hex(r, g, b):
    return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'


def extract_rgb(color_obj):
    """Extract RGB tuple from a Slides API color object."""
    if not color_obj:
        return None
    rgb = color_obj.get('rgbColor', {})
    r = rgb.get('red', 0)
    g = rgb.get('green', 0)
    b = rgb.get('blue', 0)
    return {'r': r, 'g': g, 'b': b, 'hex': rgb_to_hex(r, g, b)}


def emu_to_pt(emu):
    """Convert EMU (English Metric Units) to points."""
    return round(emu / 12700, 1)


def extract_text_styles(shape):
    """Extract all text styles from a shape's text content."""
    styles = []
    text = shape.get('text', {})
    for te in text.get('textElements', []):
        tr = te.get('textRun', {})
        if not tr:
            continue
        style = tr.get('style', {})
        entry = {}
        entry['font'] = style.get('fontFamily', None)
        fs = style.get('fontSize', {})
        entry['size_pt'] = fs.get('magnitude', None) if fs else None
        entry['bold'] = style.get('bold', False)
        entry['italic'] = style.get('italic', False)

        fg = style.get('foregroundColor', {}).get('opaqueColor', {})
        if fg:
            entry['color'] = extract_rgb(fg)

        content = tr.get('content', '').strip()
        if content:
            entry['snippet'] = content[:60]

        if entry.get('font') or entry.get('color'):
            styles.append(entry)

    return styles


def classify_slide(elements, text_styles):
    """Heuristic classification: cover, title, section, content."""
    text_count = sum(1 for e in elements if 'shape' in e)
    max_font = 0
    for s in text_styles:
        if s.get('size_pt') and s['size_pt'] > max_font:
            max_font = s['size_pt']

    if text_count <= 2 and max_font >= 30:
        return 'cover'
    if text_count <= 3 and max_font >= 28:
        return 'title'
    if text_count <= 2 and max_font >= 24:
        return 'section'
    return 'content'


def extract_presentation(svc, pres_id):
    """Extract all style data from one presentation."""
    pres = svc.presentations().get(presentationId=pres_id).execute()

    result = {
        'id': pres_id,
        'title': pres.get('title', 'Untitled'),
        'slide_count': len(pres.get('slides', [])),
        'page_size': None,
        'slides': [],
    }

    # Page size
    ps = pres.get('pageSize', {})
    w = ps.get('width', {})
    h = ps.get('height', {})
    if w and h:
        result['page_size'] = {
            'width_emu': w.get('magnitude', 0),
            'height_emu': h.get('magnitude', 0),
            'unit': w.get('unit', 'EMU'),
        }

    for i, slide in enumerate(pres.get('slides', [])):
        slide_data = {
            'index': i,
            'object_id': slide['objectId'],
            'background': None,
            'shapes': [],
            'images': [],
            'text_styles': [],
        }

        # Page background
        bg = slide.get('slideProperties', {}).get('pageBackgroundFill', {})
        solid = bg.get('solidFill', {})
        if solid:
            c = extract_rgb(solid.get('color', {}))
            if c:
                slide_data['background'] = c

        for el in slide.get('pageElements', []):
            # Element position and size
            transform = el.get('transform', {})
            size = el.get('size', {})
            pos = {
                'translate_x': transform.get('translateX', 0),
                'translate_y': transform.get('translateY', 0),
                'width': size.get('width', {}).get('magnitude', 0),
                'height': size.get('height', {}).get('magnitude', 0),
            }

            if 'shape' in el:
                shape = el['shape']
                shape_type = shape.get('shapeType', '?')
                sp = shape.get('shapeProperties', {})
                shape_entry = {
                    'type': shape_type,
                    'position': pos,
                    'fill': None,
                    'outline': None,
                }

                # Shape fill
                fill = sp.get('shapeBackgroundFill', {}).get('solidFill', {})
                if fill:
                    c = extract_rgb(fill.get('color', {}))
                    if c:
                        shape_entry['fill'] = c

                # Outline
                outline = sp.get('outline', {})
                outline_fill = outline.get('outlineFill', {}).get('solidFill', {})
                if outline_fill:
                    c = extract_rgb(outline_fill.get('color', {}))
                    if c:
                        shape_entry['outline'] = c

                # Text styles
                text_styles = extract_text_styles(shape)
                shape_entry['text_styles'] = text_styles
                slide_data['text_styles'].extend(text_styles)

                slide_data['shapes'].append(shape_entry)

            elif 'image' in el:
                img = el['image']
                slide_data['images'].append({
                    'content_url': img.get('contentUrl', ''),
                    'source_url': img.get('sourceUrl', ''),
                    'position': pos,
                })

        # Classify slide type
        slide_data['classification'] = classify_slide(
            slide.get('pageElements', []), slide_data['text_styles']
        )

        result['slides'].append(slide_data)

    return result


def consolidate(all_data):
    """Aggregate colors, fonts, and sizes across all presentations."""
    bg_colors = Counter()
    fill_colors = Counter()
    text_colors = Counter()
    fonts = Counter()
    font_sizes = Counter()

    for pres in all_data:
        for slide in pres['slides']:
            if slide['background']:
                bg_colors[slide['background']['hex']] += 1

            for shape in slide['shapes']:
                if shape['fill']:
                    fill_colors[shape['fill']['hex']] += 1

            for ts in slide['text_styles']:
                if ts.get('color'):
                    text_colors[ts['color']['hex']] += 1
                if ts.get('font'):
                    fonts[ts['font']] += 1
                if ts.get('size_pt'):
                    font_sizes[ts['size_pt']] += 1

    return {
        'background_colors': bg_colors.most_common(20),
        'shape_fill_colors': fill_colors.most_common(20),
        'text_colors': text_colors.most_common(20),
        'fonts': fonts.most_common(20),
        'font_sizes': font_sizes.most_common(20),
    }


def print_report(all_data, summary):
    """Print a human-readable report to console."""
    print('\n' + '=' * 70)
    print('JC BITCOIN — STYLE EXTRACTION REPORT')
    print('=' * 70)

    for pres in all_data:
        print(f"\n--- {pres['title']} ({pres['slide_count']} slides) ---")
        print(f"    ID: {pres['id']}")
        if pres['page_size']:
            w = pres['page_size']['width_emu']
            h = pres['page_size']['height_emu']
            print(f"    Page size: {w} x {h} EMU ({emu_to_pt(w)} x {emu_to_pt(h)} pt)")
        for slide in pres['slides']:
            bg = slide['background']['hex'] if slide['background'] else 'none'
            imgs = len(slide['images'])
            print(f"    Slide {slide['index']:2d} [{slide['classification']:7s}] bg={bg}  "
                  f"shapes={len(slide['shapes'])} images={imgs}")

    print(f"\n{'=' * 70}")
    print('CONSOLIDATED SUMMARY')
    print('=' * 70)

    print('\nBackground Colors (by frequency):')
    for color, count in summary['background_colors']:
        print(f'  {color}  ({count} slides)')

    print('\nShape Fill Colors (by frequency):')
    for color, count in summary['shape_fill_colors']:
        print(f'  {color}  ({count} shapes)')

    print('\nText Colors (by frequency):')
    for color, count in summary['text_colors']:
        print(f'  {color}  ({count} text runs)')

    print('\nFonts (by frequency):')
    for font, count in summary['fonts']:
        print(f'  {font}  ({count} text runs)')

    print('\nFont Sizes (by frequency):')
    for size, count in summary['font_sizes']:
        print(f'  {size}pt  ({count} text runs)')

    print(f"\n{'=' * 70}")
    print('DONE')


def main():
    svc = get_slides_service()
    print('Authenticated. Extracting styles from 3 presentations...\n')

    all_data = []
    for pres_id in PRESENTATION_IDS:
        print(f'Reading {pres_id}...')
        data = extract_presentation(svc, pres_id)
        all_data.append(data)
        print(f'  -> {data["title"]} ({data["slide_count"]} slides)')

    summary = consolidate(all_data)

    # Save raw data
    output = {
        'presentations': all_data,
        'consolidated': {
            'background_colors': summary['background_colors'],
            'shape_fill_colors': summary['shape_fill_colors'],
            'text_colors': summary['text_colors'],
            'fonts': summary['fonts'],
            'font_sizes': summary['font_sizes'],
        },
    }
    OUTPUT_FILE.write_text(json.dumps(output, indent=2, default=str))
    print(f'\nRaw data saved to: {OUTPUT_FILE}')

    print_report(all_data, summary)


if __name__ == '__main__':
    main()
