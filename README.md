# The Easy Peasy Way to Stop Jerking Off

A free, open-source hackbook for men who want to break the compulsive masturbation habit and master lust, written as a sequel to [EasyPeasy](https://easypeasymethod.org/) on a Christian foundation. It's for anyone who wants out, whatever they believe.

Written in R Markdown and built with [Bookdown](https://bookdown.org), using the EasyPeasy project's layout: one `.Rmd` file per chapter.

## Status

Being written one chapter at a time. See [OUTLINE.md](OUTLINE.md) for the plan and [research/](research/) for sources.

## Build locally

```sh
Rscript -e 'install.packages(c("bookdown", "rmarkdown"))'
./build.sh   # output in _book/
```

Pushing to `main` builds the book and publishes it to GitHub Pages (see `.github/workflows/build.yml`).

## License

- Book text: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Quoted testimonies and quotations from other authors belong to their authors and are not covered by this license.
- Build code: GPLv3 (adapted from the EasyPeasy repository).
- Scripture quotations are from the World English Bible (public domain).

## Credits

Inspired by [*EasyPeasy*](https://easypeasymethod.org/) by Hackauthor² (CC BY-SA 4.0, [source](https://gitlab.com/snuggy/easypeasy)), itself based on the method of Allen Carr. This book is not affiliated with or endorsed by either.
