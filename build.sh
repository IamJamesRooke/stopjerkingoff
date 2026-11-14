#!/bin/bash
# Build the web book, PDF and EPUB into _book/
# Requires R, pandoc and a LaTeX install (tinytex). Adapted from the EasyPeasy build script (GPLv3).
set -e
Rscript -e "bookdown::render_book('index.Rmd', c('bookdown::gitbook', 'bookdown::pdf_book', 'bookdown::epub_book'))"
