#!/usr/bin/env python3
"""Write redirect pages for retired chapter URLs (run after seo.py, so they stay out of the sitemap).

GitHub Pages has no server-side redirects, so each old page is a tiny HTML file that sends
readers and search engines on at once (meta refresh, canonical link, and a script fallback).
"""
import html, sys
from pathlib import Path

SITE = "https://stopjerkingoff.com/"
book = Path(sys.argv[1] if len(sys.argv) > 1 else "_book")
src = Path(__file__).resolve().parent.parent / "site" / "redirects.txt"
n = 0
for line in src.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    old, new = line.split()
    if (book / old).exists():
        print(f"redirects: skipped {old}, a real page has that name")
        continue
    if not (book / new).exists():
        sys.exit(f"redirects: target {new} for {old} does not exist")
    e = html.escape(new, quote=True)
    (book / old).write_text(f"""<!DOCTYPE html>
<html lang="en-US"><head><meta charset="utf-8">
<title>Moved | Stop Jerking Off</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{SITE}{e}">
<meta http-equiv="refresh" content="0; url={e}">
<script>location.replace("{e}" + location.hash);</script>
</head><body><p>This chapter has moved. <a href="{e}">Continue reading</a>.</p></body></html>
""", encoding="utf-8")
    n += 1
print(f"redirects: {n} pages")
