import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/List_of_tourist_attractions"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", class_="mw-parser-output")

country_section = content.find(id="By_country").parent.parent

countries = country_section.find_all("h3")

country_names = []

for country in countries:
    name = country.get_text(strip=True)
    country_names.append(name)

print("Total countries:", len(country_names))

travel_data = []

for country in countries:
    section = country.parent.parent
    country_name = country.get_text(strip=True)

    for link in section.find_all("a"):
        name = link.get_text(strip=True)
        href = link.get("href", "")

        if (
            name
            and href.startswith("https://en.wikipedia.org/wiki/")
            and "/File:" not in href
            and "/Category:" not in href
            and "Tourism in" not in name
            and not name.startswith("List of")
            and name != country_name
            and name != "edit"
        ):
            travel_data.append(
                {"Country": country_name, "Attraction": name, "URL": href}
            )

print("Total attractions:", len(travel_data))

with open("travel_destinations.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Country", "Attraction", "URL"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(travel_data)

print("CSV file created successfully!")
