#!/bin/bash
# Build the web book and EPUB into _book/, then try the PDF.
# Requires R, pandoc and (for the PDF) a LaTeX install (tinytex). Adapted from the EasyPeasy build script (GPLv3).
set -e
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::epub_book')"
# A PDF failure shouldn't stop the website going out.
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::pdf_book')" || echo "PDF build failed; website and EPUB still published"
echo "stopjerkingoff.com" > _book/CNAME
touch _book/.nojekyll
