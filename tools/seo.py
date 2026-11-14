#!/usr/bin/env python3
"""Add SEO, social sharing and favicon tags to the built website in _book/.

Run after bookdown renders the gitbook. It replaces bookdown's own
description/Open Graph/Twitter tags with one consistent set, adds canonical
links and Book structured data, and writes sitemap.xml and robots.txt.
"""
import html, json, re, sys
from datetime import date
from pathlib import Path

SITE = "https://stopjerkingoff.com/"
TITLE = "Stop Jerking Off"
FULL_TITLE = "Stop Jerking Off: The Easy Peasy Guide to Quitting Masturbation"
DESCRIPTION = ("Stop masturbating easily, without willpower or shame. A free book in the "
               "style of EasyPeasy that takes the habit apart so you can walk away for good.")
IMAGE = SITE + "images/og-image.png"
AUTHOR = "AnotherHackAuthor"

book = Path(sys.argv[1] if len(sys.argv) > 1 else "_book")
pages = sorted(p for p in book.glob("*.html"))

STRIP = re.compile(
    r'\s*<meta\s+(?:name="(?:description|twitter:[^"]*)"|property="og:[^"]*")[^>]*>'
    r'|\s*<link\s+rel="(?:canonical|icon|shortcut icon|apple-touch-icon)"[^>]*>', re.I)

def head_tags(url, title, is_home, noindex):
    e = lambda s: html.escape(s, quote=True)
    tags = [
        f'<meta name="description" content="{e(DESCRIPTION)}" />',
        f'<link rel="canonical" href="{e(url)}" />',
        '<link rel="icon" href="images/logo.svg" type="image/svg+xml" />',
        '<link rel="icon" href="favicon.ico" sizes="any" />',
        '<link rel="apple-touch-icon" href="images/logo-180.png" />',
        '<meta name="theme-color" content="#1c1e26" />',
        f'<meta property="og:site_name" content="{TITLE}" />',
        f'<meta property="og:type" content="{"book" if is_home else "article"}" />',
        f'<meta property="og:title" content="{e(title)}" />',
        f'<meta property="og:description" content="{e(DESCRIPTION)}" />',
        f'<meta property="og:url" content="{e(url)}" />',
        f'<meta property="og:image" content="{IMAGE}" />',
        '<meta property="og:image:width" content="1200" />',
        '<meta property="og:image:height" content="630" />',
        f'<meta property="og:image:alt" content="{e(FULL_TITLE)}" />',
        '<meta name="twitter:card" content="summary_large_image" />',
        f'<meta name="twitter:title" content="{e(title)}" />',
        f'<meta name="twitter:description" content="{e(DESCRIPTION)}" />',
        f'<meta name="twitter:image" content="{IMAGE}" />',
    ]
    if noindex:
        tags.append('<meta name="robots" content="noindex" />')
    else:
        tags.append('<script src="feedback.js" defer></script>')
    # Cookie-free visit counter (GoatCounter); no personal data is collected.
    tags.append('<script data-goatcounter="https://stopjerkingoff.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>')
    if is_home:
        data = {
            "@context": "https://schema.org", "@type": "Book",
            "name": TITLE,
            "alternativeHeadline": "The Easy Peasy Guide to Quitting Masturbation",
            "description": DESCRIPTION, "url": SITE, "image": IMAGE,
            "author": {"@type": "Person", "name": AUTHOR},
            "inLanguage": "en", "isAccessibleForFree": True,
            "license": "https://creativecommons.org/licenses/by-sa/4.0/",
            "isBasedOn": "https://easypeasymethod.org/",
            "workExample": [
                {"@type": "Book", "bookFormat": "https://schema.org/EBook",
                 "encodingFormat": "application/pdf", "url": SITE + "stopjerkingoff.pdf"},
                {"@type": "Book", "bookFormat": "https://schema.org/EBook",
                 "encodingFormat": "application/epub+zip", "url": SITE + "stopjerkingoff.epub"},
            ],
        }
        tags.append('<script type="application/ld+json">' + json.dumps(data) + '</script>')
    return "\n".join(tags) + "\n"

listed = []
for p in pages:
    name = p.name
    is_home = name == "index.html"
    noindex = name == "404.html"
    url = SITE if is_home else SITE + name
    s = p.read_text(encoding="utf-8")
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    page_title = html.unescape(m.group(1).strip()) if m else TITLE
    if is_home:
        title = FULL_TITLE
    elif name == "404.html":
        title = "Page not found | " + TITLE
    else:
        chapter = re.split(r"\s+\|\s+", page_title)[0].strip()
        title = TITLE if chapter in ("", TITLE) else f"{chapter} | {TITLE}"
    if m:
        s = s[:m.start()] + f"<title>{html.escape(title)}</title>" + s[m.end():]
    s = STRIP.sub("", s)
    if name == "introduction.html":
        url = SITE  # canonical points at the homepage copy
    s = s.replace("</head>", head_tags(url, title, is_home, noindex) + "</head>", 1)
    p.write_text(s, encoding="utf-8")
    if not noindex and name != "introduction.html":  # duplicate of the homepage
        listed.append(SITE if is_home else SITE + name)

today = date.today().isoformat()
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in listed]
sm.append("</urlset>")
(book / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
(book / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
print(f"SEO tags added to {len(pages)} pages; sitemap lists {len(listed)}")
