# Stop Jerking Off: The Easy Peasy Way to Conquer Lust

**Read it at [stopjerkingoff.com](https://stopjerkingoff.com/)**, online or as a PDF or EPUB.

A book for men who want to stop masturbating, quit porn and stop making bad decisions about women, without willpower or shame. It is inspired by [EasyPeasy](https://easypeasymethod.org/) and written on a Christian foundation, for anyone who wants out, whatever they believe.

The text is open. Suggestions, corrections and pull requests are welcome: see **[CONTRIBUTING.md](CONTRIBUTING.md)**.

## How the repository is laid out

| Path | What it holds |
| --- | --- |
| `chapters/` | The book itself, one Markdown file per chapter, in reading order by file number. `00-introduction.md` is the Introduction. |
| `pages/` | Website-only pages: the FAQ, the About page and the "Why this book" article. They are not in the PDF or EPUB. |
| `index.Rmd` | The book's settings (title, description, language) and the website's cover and download buttons. |
| `_bookdown.yml` | The chapter order for the website, the PDF and the EPUB. A new chapter must be added to all three lists. |
| `_output.yml` | Output settings for the website, the PDF and the EPUB. |
| `style.css`, `site/` | Website design and scripts (sharing buttons, visitor count, feedback box). |
| `preamble.tex`, `tools/dropcap.lua` | The print design of the PDF (5.5 × 8.5 in trade paperback). |
| `epub.css`, `epub-metadata.xml`, `tools/epub.lua` | The EPUB design and metadata. |
| `tools/seo.py` | Adds search and sharing metadata, the sitemap and `llms.txt` to the built website. |
| `images/` | Cover, logo and share image. |
| `editorial/` | The editing team's working notes: style brief, outline, book bible, reviews, open issues. |
| `research/` | Sources, testimonies and quote checks behind the book. |
| `launch/` | Launch and promotion notes. |
| `worker/` | An optional Cloudflare Worker for the website's feedback box. |
| `archive/` | Old branding and drafts, kept for reference. Nothing here is used by the build. |

## Build it yourself

You need [R](https://www.r-project.org/), [pandoc](https://pandoc.org/) and, for the PDF, a LaTeX install with XeLaTeX (for example [TinyTeX](https://yihui.org/tinytex/)).

```sh
Rscript -e 'install.packages(c("bookdown", "rmarkdown"))'
./build.sh                    # website, EPUB and PDF, into _book/
BUILD_FORMATS=0 ./build.sh    # website only (much faster)
```

Open `_book/index.html` in a browser to read the result.

## How it is published

- Every push to `main` rebuilds the website and publishes it to GitHub Pages ([`build.yml`](.github/workflows/build.yml)).
- The PDF and EPUB are rebuilt every night, or on demand, by [`formats.yml`](.github/workflows/formats.yml). It stores them on the `formats` release, and the website serves them from there.

## License

- **Book text:** [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). You may copy, share, print, translate and adapt it, for any purpose, as long as you give credit and release your version under the same license. Quoted testimonies and quotations from other writers belong to their authors and are not covered by this license.
- **Build code:** GPLv3 (adapted from the EasyPeasy repository). See [LICENSE](LICENSE).
- **Scripture:** quotations are from the World English Bible, which is in the public domain.

## Credits

The structure and method are inspired by [*EasyPeasy*](https://easypeasymethod.org/) by Hackauthor² (CC BY-SA 4.0, [source](https://gitlab.com/snuggy/easypeasy)), which is itself based on Allen Carr's Easyway method. This book is not affiliated with or endorsed by either. Full credits are in the book's [Attribution](chapters/attribution.md) chapter.
