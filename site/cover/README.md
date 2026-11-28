Source for the book cover and share image. To re-render after a change (needs Node and Playwright):

    node site/cover/shot.js cover.html 1600 2560 images/cover.png
    node site/cover/shot.js og.html 1200 630 images/og-image.png

Then bump `?v=` on IMAGE in tools/seo.py so social sites refetch the share image.

Old branding (droplet logo, charcoal cover, 2026-11-14 to 2026-11-17) is kept in archive/cover/2026-11-17/ and archive/images/2026-11-17-old-branding/ (the unused share-image drafts og-A and og-B are in archive/cover/og-drafts/).

The share image is built around the hook, not the title (2026-11-28): on X the title strip and the domain already carry the name. It uses the drawing images/illustrations/intro-back-room.svg. The earlier title-led share image is in archive/cover/2026-11-28-title-share-image/.
