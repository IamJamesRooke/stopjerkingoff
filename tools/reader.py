#!/usr/bin/env python3
"""Reading aids for the built website in _book/ (run after seo.py).

- "Chapter N of T · about X min" under each chapter title.
- A big "Next chapter" card at the end of each chapter.
- A one-screen homepage: cover, a one-line pitch (site/hero-line.txt, else the book's first line), a few facts, "Start reading".
- Loads site/reader.js, which remembers the last chapter read (on the device only)
  and offers "Continue reading", and draws a thin progress bar.
"""
import html, math, re, sys, time
from pathlib import Path

book = Path(sys.argv[1] if len(sys.argv) > 1 else "_book")
WPM = 230  # a relaxed adult reading speed
WEB_ONLY = {"faq.html", "about.html", "why-this-book.html", "index.html", "404.html"}
VERSION = str(int(time.time()))

# Reading order = the top-level entries of the sidebar, as bookdown wrote them.
home = (book / "introduction.html").read_text(encoding="utf-8")
order, titles = [], {}
for m in re.finditer(r'<li class="chapter" data-level="[^".]*" data-path="([^"]+)"><a href="\1">(.*?)</a>', home):
    path, label = m.group(1), m.group(2)
    if path in titles or path in WEB_ONLY:
        continue
    label = re.sub(r"<i[^>]*></i>|<b>[^<]*</b>", "", label)
    titles[path] = html.unescape(re.sub(r"<[^>]+>", "", label)).strip()
    order.append(path)

def body_of(s):
    m = re.search(r'<section class="normal"[^>]*>(.*?)</section>', s, re.S)
    return m.group(1) if m else ""

def words(s):
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body_of(s), flags=re.S)
    return len(re.sub(r"<[^>]+>", " ", text).split())

pages = {p: (book / p).read_text(encoding="utf-8") for p in order}
minutes = {p: max(1, round(words(s) / WPM)) for p, s in pages.items()}
# Chapter numbers are the book's own (bookdown's), so the site, PDF and EPUB agree.
def number_of(s):
    m = re.search(r'class="section level1[^"]*"[^>]*>\s*<h1><span class="header-section-number">\D*(\d+)</span>', s)
    return int(m.group(1)) if m else None
numbers = {p: number_of(s) for p, s in pages.items()}
counted = [p for p in order if numbers[p]]
total = max([n for n in numbers.values() if n] or [0])
hours = sum(minutes.values()) / 60
e = lambda t: html.escape(t, quote=True)

def meta_line(p):
    n = f"Chapter {numbers[p]} of {total} · " if numbers[p] else ""
    return (f'<p class="chapter-meta" data-path="{e(p)}" data-title="{e(titles[p])}">'
            f'{n}about {minutes[p]} min</p>')

def next_card(p):
    i = order.index(p)
    if i + 1 >= len(order):
        return ""
    nxt = order[i + 1]
    label = "Next chapter" if nxt in counted else "Next"
    return (f'<nav class="next-card" aria-label="Next chapter"><a href="{e(nxt)}">'
            f'<span class="next-label">{label}</span>'
            f'<span class="next-title">{e(titles[nxt])}</span>'
            f'<span class="next-meta">about {minutes[nxt]} min &rarr;</span></a></nav>')

SCRIPT = f'<script src="reader.js?v={VERSION}" defer></script>'

def finish(s):
    return s.replace("</head>", SCRIPT + "\n</head>", 1)

for p in order:
  # the homepage is a copy of the Introduction, so it gets the same treatment
  for target in [p] + (["index.html"] if p == "introduction.html" and (book / "index.html").exists() else []):
    s = pages[p] if target == p else (book / target).read_text(encoding="utf-8")
    # the meta line goes right after the chapter's own title
    s = re.sub(r'(<div id="[^"]+" class="section level1[^"]*"[^>]*>\s*<h1>.*?</h1>)',
               lambda m: m.group(1) + "\n" + meta_line(p), s, count=1, flags=re.S)
    # the card goes at the end of the chapter text
    i = s.find('<section class="normal"')
    j = s.find("</section>", i)
    if i >= 0 and j > 0:
        s = s[:j] + next_card(p) + "\n" + s[j:]
    (book / target).write_text(s if target == "index.html" else finish(s), encoding="utf-8")

# Homepage: one screen that says what the book is and starts it.
first = order[1] if len(order) > 1 else "introduction.html"
for name in ("index.html", "introduction.html"):
    f = book / name
    if not f.exists():
        continue
    s = f.read_text(encoding="utf-8")
    cover = re.search(r'<img class="home-cover"[^>]*>', s)
    intro = re.search(r'<div id="introduction"[^>]*>.*?<p>(.*?)</p>', s, re.S)
    if not cover or not intro:
        continue
    s = s.replace(cover.group(0), "", 1)
    s = re.sub(r'<div class="downloads">.*?</div>\s*', "", s, count=1, flags=re.S)
    line = re.split(r"(?<=[.!?])\s", re.sub(r"<[^>]+>", "", intro.group(1)).strip())[0]
    # the homepage line is a pitch of its own (site/hero-line.txt); the book's first line is the fallback
    pitch = Path(__file__).resolve().parent.parent / "site" / "hero-line.txt"
    if pitch.exists() and pitch.read_text(encoding="utf-8").strip():
        line = e(pitch.read_text(encoding="utf-8").strip())
    hero = f'''<div class="home-hero">
{cover.group(0)}
<div class="hero-text">
<p class="hero-line">{line}</p>
<p class="hero-facts">{total} short chapters · about {round(hours)} hours · read here or download</p>
<p class="hero-actions"><a class="hero-start" href="#introduction">Start reading</a>
<a class="hero-continue" href="{e(first)}" hidden>Continue</a></p>
<p class="hero-downloads">Or download the <a href="stopjerkingoff.pdf">PDF</a> or the <a href="stopjerkingoff.epub">EPUB</a>.</p>
</div>
</div>
'''
    # the title block becomes the hero; the h1 stays for search engines and screen readers
    s = re.sub(r'<div id="header">(.*?)</div>', lambda m: '<div id="header" class="sr-only">' + m.group(1) + "</div>\n" + hero, s, count=1, flags=re.S)
    f.write_text(finish(s) if name == "index.html" else s, encoding="utf-8")

print(f"Reading aids: {total} numbered chapters, about {hours:.1f} hours, {len(order)} pages")
