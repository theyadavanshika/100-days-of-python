# Zillow Clone Scraper → Google Form Submitter

Scrapes property listings from a demo real estate site and submits each one as a separate response on a Google Form.

## What it does

1. **Scrapes** the [App Brewery Zillow Clone](https://appbrewery.github.io/Zillow-Clone/) using `requests` and `BeautifulSoup`, collecting each listing's address, price, and link.
2. **Fills out a Google Form** with Selenium — one submission per listing — reloading the form between entries.

## How it works

**Part 1 — Scraping**
- Fetches the Zillow Clone page and parses it with BeautifulSoup.
- Finds every `data-test="property-card"` element on the page.
- For each card, pulls:
  - **Address** — from `data-test="property-card-addr"`, whitespace stripped.
  - **Price** — from `data-test="property-card-price"`, with trailing bits like `+`, `/mo`, or anything after a space stripped off, leaving just the base number.
  - **Link** — the `href` attribute from `data-test="property-card-link"`.

**Part 2 — Form filling**
- Waits until a text field is visible on the open form.
- For each listing: grabs the currently visible text inputs, types address → field 1, price → field 2, link → field 3, then clicks **Submit**.
- Reloads the form and pauses before moving on to the next listing.

## Requirements

- Python 3.8+
- Google Chrome
- A Google Form with **exactly three short-answer text questions**, in this order:
  1. Address
  2. Price
  3. Link

  The script fills fields by position, not by label, so the order matters more than the wording of the questions.

Install the Python packages:

```bash
pip install requests beautifulsoup4 selenium
```

> Selenium 4.6+ bundles Selenium Manager, which downloads a matching ChromeDriver automatically. On an older version, install [ChromeDriver](https://chromedriver.chromium.org/) yourself and make sure it's on your PATH.

## Setup

1. Create the Google Form described above and copy its **live link** — the one ending in `/viewform`, not the `/edit` editor link.
2. Open the script and replace the placeholder:

   ```python
   GOOGLE_FORM_URL = "YOUR_GOOGLE_FORM_URL"
   ```

   with your form's actual URL. 

## Usage

```bash
python scraper.py
```

*(Swap `scraper.py` for whatever you named the file.)*

A Chrome window opens automatically, loads the form, scrapes the listings in the background, then fills in and submits the form once per listing — reloading it in between. Because the driver launches with `detach: True`, Chrome stays open after the script finishes, so close it manually when you're done.

## Limitations

- **Fixed field order** — adding, removing, or reordering questions on the form will misalign the submitted data.
- **Static waits** (`time.sleep`) drive most of the timing rather than dynamic waits, so a slow connection could cause a field to be missed.
- **Selector-dependent** — if App Brewery updates the clone site's markup, or Google changes its form's HTML, the script will need updating.
- **No error handling** — one failed submission stops the whole run.
- **Demo site only** — this targets the App Brewery clone specifically and won't work against the real zillow.com, which uses different markup and has bot protections.

## Possible improvements

- Replace `time.sleep()` calls with `WebDriverWait` conditions throughout.
- Wrap each submission in `try/except` so one failure doesn't halt the batch.
- Add a headless Chrome option for running without a visible browser window.
- Move `GOOGLE_FORM_URL` into an environment variable instead of hardcoding it.