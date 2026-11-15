Source for the book cover and share image. To re-render after a change (needs Node and Playwright):

    node site/cover/shot.js cover.html 1600 2560 images/cover.png
    node site/cover/shot.js og.html 1200 630 images/og-image.png

Then bump `?v=` on IMAGE in tools/seo.py so social sites refetch the share image.
