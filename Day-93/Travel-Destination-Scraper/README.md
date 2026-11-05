# Travel Destination Web Scraper

A Python web scraping project that extracts tourist destinations and country information from Wikipedia and stores the collected data in a CSV file.

## Features
- Scrapes country names from Wikipedia.
- Extracts tourist attraction links.
- Collects country names, attraction names, and URLs.
- Exports the collected data into a CSV file.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- CSV

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Output

The scraper generates `travel_destinations.csv` containing:
- Country
- Attraction
- URL

## What I Learned
- Sending HTTP requests using Requests.
- Parsing HTML using BeautifulSoup.
- Navigating HTML elements and extracting links.
- Filtering scraped data.
- Writing data into CSV files.

## Disclaimer
This project is created for educational purposes. Data is collected from Wikipedia and may change as the website is updated.