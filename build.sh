#!/bin/bash
# Build the web book and EPUB into _book/, then try the PDF.
# Requires R, pandoc and (for the PDF) a LaTeX install (tinytex). Adapted from the EasyPeasy build script (GPLv3).
set -e
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"
# The EPUB and PDF are slow, so the site deploy skips them (BUILD_FORMATS=0) and reuses the
# latest copies built by .github/workflows/formats.yml. Run locally, this builds everything.
if [ "${BUILD_FORMATS:-1}" = "1" ]; then
  Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::epub_book')"
  # A PDF failure shouldn't stop the website going out.
  Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::pdf_book')" || echo "PDF build failed; website and EPUB still published"
fi
# The first page is named introduction.html, so give the site root a homepage.
[ -f _book/index.html ] || cp _book/introduction.html _book/index.html
cp -r images _book/
cp images/favicon.ico _book/favicon.ico
cp site/feedback.js _book/feedback.js
cp site/counter.js _book/counter.js
cp site/share.js _book/share.js
cp site/reader.js _book/reader.js
cp site/*.txt _book/  # IndexNow key file
python3 tools/seo.py _book
python3 tools/reader.py _book
python3 tools/redirects.py _book
echo "stopjerkingoff.com" > _book/CNAME
touch _book/.nojekyll
