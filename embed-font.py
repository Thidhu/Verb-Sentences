"""Optional: bake your font INTO index.html so it can never go missing.
Usage:  python3 embed-font.py fonts/CustomFont.woff2
Creates index-single-file.html (works even if the fonts/ folder is not uploaded)."""
import base64, re, sys, os
if len(sys.argv) < 2:
    sys.exit("Usage: python3 embed-font.py fonts/CustomFont.woff2")
path = sys.argv[1]
ext = os.path.splitext(path)[1].lower().lstrip('.')
fmt = {'woff2': 'woff2', 'woff': 'woff', 'ttf': 'truetype', 'otf': 'opentype'}[ext]
mime = {'woff2': 'font/woff2', 'woff': 'font/woff', 'ttf': 'font/ttf', 'otf': 'font/otf'}[ext]
b64 = base64.b64encode(open(path, 'rb').read()).decode()
face = ("/*FONT_FACE_START*/\n@font-face{font-family:'CustomFont';"
        "src:url(data:%s;base64,%s) format('%s');"
        "font-weight:100 900;font-style:normal;font-display:swap;}\n/*FONT_FACE_END*/") % (mime, b64, fmt)
html = open('index.html', encoding='utf-8').read()
html = re.sub(r'/\*FONT_FACE_START\*/.*?/\*FONT_FACE_END\*/', lambda m: face, html, flags=re.S)
html = re.sub(r'<link rel="preload" href="fonts/CustomFont.woff2"[^>]*>\n?', '', html)
open('index-single-file.html', 'w', encoding='utf-8').write(html)
print('Done: index-single-file.html (%d KB)' % (len(html) // 1024))
