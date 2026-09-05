import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_URL = "YOUR_GOOGLE_FORM_URL"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM_URL) 
time.sleep(5)

wait = WebDriverWait(driver, 10)

response = requests.get(ZILLOW_CLONE_URL)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title) 

property_cards = soup.find_all(attrs={"data-test": "property-card"})

property_links = []
property_prices = []
property_addresses = []

for card in property_cards:

    link = card.find("a", attrs={"data-test": "property-card-link"})
    property_links.append(link.get("href"))

    price = card.find(attrs={"data-test": "property-card-price"})
    property_prices.append(price.text.split("+")[0].split("/")[0].split(" ")[0])

    address = card.find(attrs={"data-test": "property-card-addr"}) 
    property_addresses.append(address.text.strip())

#--------------------------------------Part-2------------------------------------#
wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[type='text']") 
    )
)

for i in range(len(property_addresses)):

    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    visible_inputs = [input for input in inputs if input.is_displayed()]
 
    # print("No. of visible fields:", len(visible_inputs))  
    visible_inputs[0].send_keys(property_addresses[i]) 
    visible_inputs[1].send_keys(property_prices[i])
    visible_inputs[2].send_keys(property_links[i])

    submit_button = driver.find_element(By.XPATH, value="//span[text()='Submit']")
    submit_button.click()

    print(f"Property {i+1} submitted!") 

    time.sleep(2)
    driver.get(GOOGLE_FORM_URL) 
    time.sleep(5)
    



