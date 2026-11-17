#!/usr/bin/env python3
"""Add SEO, social sharing and favicon tags to the built website in _book/.

Run after bookdown renders the gitbook. It replaces bookdown's own
description/Open Graph/Twitter tags with one consistent set, adds canonical
links and Book structured data, and writes sitemap.xml and robots.txt.
"""
import html, json, re, sys
from datetime import date
import time
from pathlib import Path

SITE = "https://stopjerkingoff.com/"
TITLE = "Stop Jerking Off"
FULL_TITLE = "Stop Jerking Off: The Easy Peasy Way to Conquer Lust"
DESCRIPTION = ("Conquer lust the easy way: stop masturbating and watching porn without willpower or shame. "
               "A free book in the style of EasyPeasy that helps you walk away for good.")
IMAGE = SITE + "images/og-image.png?v=6"
PUBLISHER = {"@type": "Organization", "name": TITLE, "url": SITE}  # the book is anonymous
# Search-engine ownership checks: paste the code from Google Search Console / Bing Webmaster Tools here.
GOOGLE_VERIFY = ""
BING_VERIFY = ""

book = Path(sys.argv[1] if len(sys.argv) > 1 else "_book")
pages = sorted(p for p in book.glob("*.html"))

STRIP = re.compile(
    r'\s*<meta\s+(?:name="(?:description|twitter:[^"]*)"|property="og:[^"]*")[^>]*>'
    r'|\s*<link\s+rel="(?:canonical|icon|shortcut icon|apple-touch-icon)"[^>]*>', re.I)

def head_tags(url, title, is_home, noindex, desc=DESCRIPTION, extra_ld=None):
    e = lambda s: html.escape(s, quote=True)
    tags = [
        f'<meta name="description" content="{e(desc)}" />',
        f'<link rel="canonical" href="{e(url)}" />',
        '<link rel="icon" href="images/logo.svg" type="image/svg+xml" />',
        '<link rel="icon" href="favicon.ico" sizes="any" />',
        '<link rel="apple-touch-icon" href="images/logo-180.png" />',
        '<meta name="theme-color" content="#17181b" />',
        '<link rel="preconnect" href="https://fonts.googleapis.com" />',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&display=swap" />',
        f'<meta property="og:site_name" content="{TITLE}" />',
        f'<meta property="og:type" content="{"book" if is_home else "article"}" />',
        f'<meta property="og:title" content="{e(title)}" />',
        f'<meta property="og:description" content="{e(desc)}" />',
        f'<meta property="og:url" content="{e(url)}" />',
        f'<meta property="og:image" content="{IMAGE}" />',
        '<meta property="og:image:width" content="1200" />',
        '<meta property="og:image:height" content="630" />',
        f'<meta property="og:image:alt" content="{e(FULL_TITLE)}" />',
        '<meta name="twitter:card" content="summary_large_image" />',
        f'<meta name="twitter:title" content="{e(title)}" />',
        f'<meta name="twitter:description" content="{e(desc)}" />',
        f'<meta name="twitter:image" content="{IMAGE}" />',
    ]
    if is_home and GOOGLE_VERIFY:
        tags.append(f'<meta name="google-site-verification" content="{e(GOOGLE_VERIFY)}" />')
    if is_home and BING_VERIFY:
        tags.append(f'<meta name="msvalidate.01" content="{e(BING_VERIFY)}" />')
    if noindex:
        tags.append('<meta name="robots" content="noindex" />')
    else:
        tags.append('<script src="feedback.js" defer></script>')
        tags.append('<script src="counter.js" defer></script>')
        tags.append('<script src="share.js" defer></script>')
    # Cookie-free visit counter (GoatCounter); no personal data is collected.
    tags.append('<script data-goatcounter="https://stopjerkingoff.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>')
    if is_home:
        data = {
            "@context": "https://schema.org", "@type": "Book",
            "name": TITLE,
            "alternativeHeadline": "The Easy Peasy Way to Conquer Lust",
            "description": DESCRIPTION, "url": SITE, "image": IMAGE,
            "publisher": PUBLISHER,
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
    if extra_ld:
        tags.append('<script type="application/ld+json">' + json.dumps(extra_ld) + '</script>')
    return "\n".join(tags) + "\n"


# Map each page to its chapter file so the toolbar's Edit button works.
# bookdown leaves "%s" unfilled in this merged build, so fill it here.
EDIT_BASE = "https://github.com/IamJamesRooke/stopjerkingoff/edit/main/"
def pandoc_id(text):
    m = re.search(r"\{[^}]*#([\w.-]+)[^}]*\}", text)
    if m:
        return m.group(1)
    text = re.sub(r"\{[^}]*\}", "", text).strip().lower()
    text = re.sub(r"[^\w\s.-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return re.sub(r"^[^a-z]+", "", text)
SOURCES = {}

# Website-only pages: their own descriptions and structured data.
PAGE_DESC = {
    "faq.html": ("How do I stop masturbating? Can I quit without willpower? Is it harmful, or a sin? "
                 "Plain answers to the questions men ask most, from the free book Stop Jerking Off."),
    "why-this-book.html": ("Why willpower, streaks and NoFap counters keep failing, and how a free book in the "
                           "style of EasyPeasy helps men conquer lust and stop masturbating for good."),
}

def text_of(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()

def faq_ld(s):
    """FAQPage data from each h2 question and the paragraphs under it."""
    items = []
    for block in re.findall(r'<div id="[^"]*" class="section level2[^"]*">(.*?)</div>', s, re.S):
        q = re.search(r"<h2[^>]*>(.*?)</h2>", block, re.S)
        paras = re.findall(r"<p>(.*?)</p>", block, re.S)
        if q and paras:
            items.append({"@type": "Question", "name": text_of(q.group(1)),
                          "acceptedAnswer": {"@type": "Answer", "text": " ".join(text_of(x) for x in paras)}})
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}

def article_ld(url, title, desc):
    return {"@context": "https://schema.org", "@type": "Article", "headline": title,
            "description": desc, "url": url, "image": IMAGE,
            "author": PUBLISHER, "publisher": PUBLISHER,
            "about": {"@type": "Book", "name": TITLE, "url": SITE}}
for rmd in sorted(Path(".").glob("*.Rmd")):
    for line in rmd.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            SOURCES[pandoc_id(line[2:])] = rmd.name
            break
SOURCES["index"] = "index.Rmd"
EDIT_PLACEHOLDER = EDIT_BASE + "%s"

def chapter_desc(s):
    """A page's own search description: its opening paragraph (after any epigraph), about 155 characters."""
    body = s.split("<h1", 1)[-1]
    body = re.sub(r"<blockquote.*?</blockquote>", "", body, flags=re.S)
    text = ""
    for para in re.findall(r"<p>(.*?)</p>", body, re.S):
        t = text_of(para)
        if not t or t.isupper():
            continue
        text = (text + " " + t).strip()
        if len(text) >= 90:
            break
    if not text:
        return DESCRIPTION
    if len(text) > 158:
        text = text[:155].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return text

VERSION = str(int(time.time()))
listed = []
entries = []
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
    src = SOURCES.get(name[:-5])
    s = s.replace(EDIT_PLACEHOLDER, EDIT_BASE + src if src else "https://github.com/IamJamesRooke/stopjerkingoff")
    if name == "introduction.html":
        url = SITE  # canonical points at the homepage copy
    # Put the homepage cover above the "Introduction" heading.
    m = re.search(r'(?:<p>)?\s*(<img class="home-cover"[^>]*>)\s*(?:</p>)?', s)
    if m:
        s = s[:m.start()] + s[m.end():]
        # Above the title block, inside the reading area (never in the toolbar).
        anchor = '<div id="header">' if '<div id="header">' in s else '<section class="normal"'
        if anchor == '<div id="header">':
            s = s.replace(anchor, m.group(1) + "\n" + anchor, 1)
        else:
            s = re.sub(r'(<section class="normal"[^>]*>)', lambda x: x.group(1) + "\n" + m.group(1), s, count=1)
    desc = PAGE_DESC.get(name) or (DESCRIPTION if is_home or noindex else chapter_desc(s))
    extra = faq_ld(s) if name == "faq.html" else article_ld(url, title.split(" | ")[0], desc) if name == "why-this-book.html" else None
    s = s.replace("</head>", head_tags(url, title, is_home, noindex, desc, extra) + "</head>", 1)
    # Cache-bust our own files so readers get new styles and scripts right after a deploy.
    s = re.sub(r'(href|src)="(style\.css|feedback\.js|counter\.js|share\.js)"', lambda m: f'{m.group(1)}="{m.group(2)}?v={VERSION}"', s)
    p.write_text(s, encoding="utf-8")
    if not noindex and name != "introduction.html":  # duplicate of the homepage
        listed.append(SITE if is_home else SITE + name)
        if not is_home:
            entries.append((SOURCES.get(name[:-5], "zz"), title.split(" | ")[0], SITE + name, desc))

today = date.today().isoformat()
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in listed]
sm.append("</urlset>")
(book / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
# Search engines and AI assistants are all welcome to read and cite the book.
BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
        "PerplexityBot", "Perplexity-User", "Google-Extended", "Googlebot", "Bingbot", "Applebot",
        "Applebot-Extended", "DuckDuckBot", "CCBot", "Meta-ExternalAgent", "MistralAI-User"]
robots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in BOTS)
robots += f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n"
(book / "robots.txt").write_text(robots, encoding="utf-8")

# llms.txt (llmstxt.org): a plain summary for AI assistants, with every page listed.
def section(names):
    return "".join(f"- [{t}]({u}): {d}\n" for _, t, u, d in entries if u.rsplit("/", 1)[-1] in names)
special = {"faq.html", "why-this-book.html", "attribution.html"}
chapters = "".join(f"- [{t}]({u}): {d}\n" for _, t, u, d in sorted(entries) if u.rsplit("/", 1)[-1] not in special)
llms = f"""# {FULL_TITLE}

> A free, complete book that helps men conquer lust without willpower, streak counters or shame: stop masturbating, stop watching porn, and stop making bad decisions with women because they are thinking with the wrong head. It works like EasyPeasy (the free book for quitting porn) and Allen Carr's Easy Way to Stop Smoking: it removes the beliefs that make the habit feel worth keeping, so stopping becomes easy. Written from a Christian point of view, and it also works for readers who aren't religious.

- Free to read online at {SITE}, with no ads and no sign-up. Also free as a PDF ({SITE}stopjerkingoff.pdf) and EPUB ({SITE}stopjerkingoff.epub).
- Takes a few hours to read. Readers keep living normally until they finish, then stop.
- No streak counting, no cutting down, no substitutes, and no fortress of blockers held up by willpower. A slip is not a "relapse"; wet dreams and morning erections are not slips.
- Makes no medical claims: it accepts that doctors say masturbation doesn't harm the body, and focuses on mind, drive, self-control and faith. No "superpowers" or testosterone promises.
- A spiritual successor to EasyPeasy (https://easypeasymethod.org/), by a different author, not an official sequel. It covers porn as well; EasyPeasy is still recommended reading.
- Licence: CC BY-SA 4.0. Published anonymously: the book is about the reader, not the writer.
- Good fit for: men who want to stop masturbating or watching porn, men who quit porn but still masturbate, men whose lust drives how they treat women, NoFap users tired of resetting counters, Christian men struggling with lust, married men, and wives, parents or pastors trying to help someone.

## Start here

- [Home and Introduction]({SITE}): what the book is and how to read it.
{section({"faq.html", "why-this-book.html"})}
## Chapters

{chapters}
## Optional

{section({"attribution.html"})}"""
(book / "llms.txt").write_text(llms, encoding="utf-8")
print(f"SEO tags added to {len(pages)} pages; sitemap lists {len(listed)}")
