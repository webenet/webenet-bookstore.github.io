# WEBENET — Online Bookstore

**Books for a Brighter You.** A responsive, single-page, English-language bookstore storefront with **144 actual published titles across 12 genres**.

## Open the website

1. Extract the ZIP archive completely.
2. Open `index.html` in a modern browser. No installation or build process is required.
3. Use the genre filters, search bar, sorting, book details, favorites and shopping bag.
4. Connect to the internet for **actual edition cover images** fetched on demand from Open Library. Book images are retrieved through the search API and Covers API, checked against title and author before they are displayed. **The ZIP does not include the book covers.** A fallback shows title and author if a matching cover cannot be loaded.

You can also publish these files to a GitHub Pages repository: upload the content of this folder to its root and enable Pages for the main branch.

## Included

- 144 real, unique books, 12 genres (12 titles each): Horror; Action & Adventure; Romance; Mystery & Thriller; Fantasy; Science Fiction; Literary Classics; Young Adult; Personal Growth; Business & Finance; History & Biography; Kids & Family.
- Responsive desktop/mobile layout, genuine WEBENET logo, categories, search, sorting, favorites, book details, and quantity-based shopping bag.
- A demo catalog with USD price reference amounts.
- **10 selected prices with external source references** (publisher/retailer information consulted in September 2026; check current edition, region and availability). Other prices are **illustrative estimates**, not independently checked or suitable for live sales without further verification.
- Distinct demo customer-support and advisory phone numbers. **Replace both before launch:** `+1 (202) 555-0142` and `+1 (202) 555-0143` are fictional North American sample numbers, not working WEBENET support channels.
- Local persistence for favorites, bag, and resolved cover URLs when the browser permits local storage.

## Important limitations before launching an actual store

- **Checkout is a demo**, not a payment processor. No orders or payments are accepted. Connect a real payment service and order backend before enabling sales.
- Inventory, shipping rates, taxes, returns policy, legal business address, privacy policy and contact channels have not been configured.
- Display prices are **not a guarantee of current sale price**. Confirm pricing, specific ISBN/format, availability, distribution rights, and any image permissions with the supplier.
- Open Library cover service is external: a cover can be unavailable or loading can fail because of network, service restrictions, or missing edition data. Do not describe fallback text as cover photography.
- Avoid using another retailer's physical address or customer-support numbers as your own.

## Project files

```text
index.html                  Entry point and store layout
css/style.css               Responsive styling
js/app.js                   Search, cart, favorites, covers, UI
js/catalog.js               Catalog bundled for file:// use
data/books.json             Readable source catalog
assets/webenet-logo.webp    Brand logo (optimized, < 1 MB)
assets/favicon.png          Square favicon master with book emblem
assets/favicon-32.png       32x32 browser-tab icon
assets/apple-touch-icon.png 180x180 iOS homescreen icon
favicon.ico                 Multi-resolution browser-tab icon
preview.png                 Preview of the local offline layout
```

To change titles or prices, edit `build_catalog.py` and run `python build_catalog.py`, then replace any titles or pricing references responsibly. You may also edit `data/books.json` and synchronize `js/catalog.js` manually. To change contact numbers, update the `#contact` section in `index.html`.

## External cover sources

- [Open Library Covers API](https://openlibrary.org/dev/docs/api/covers)
- [Open Library Search API](https://openlibrary.org/dev/docs/api/search)

Open Library's API is used for book metadata and third-party book covers. The images remain the property of their respective rights holders and/or are made available under the applicable service terms.

## Price reference examples

- [The Shining — publisher paperback price](https://www.penguinrandomhouse.com/books/92991/the-shining-by-stephen-king/)
- [It — retailer paperback edition](https://www.barnesandnoble.com/w/it-stephen-king/1100623119?ean=9781501182099)
- [Independent bookstore bestseller list — Project Hail Mary, Red Rising, Dungeon Crawler Carl](https://www.bookweb.org/news/indie-scififantasy-bestseller-list-1632923)

See `data/books.json` for the complete set of sourced items and links. WEBENET is not affiliated with those publishers or retailers.

© 2026 WEBENET. Storefront demonstration.

## Logo and favicon

The header and footer display `assets/webenet-logo.webp`, while the browser tab uses the icon-sized open-book emblem in `favicon.ico` / `assets/favicon-32.png`. The HTML links include a query version to refresh browser favicon caches after uploading. Upload **all files and folders inside this ZIP**, not just `index.html`, to the root of the GitHub Pages repository. If the old tab icon remains, perform a hard refresh or open the page in a fresh private window.
