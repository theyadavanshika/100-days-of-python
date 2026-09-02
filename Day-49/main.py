import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------------------ Constants ----------------------------- #
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/" 
ALLOWED_CLASSES = ["Yoga Class", "Spin Class", "HIIT Class"] 
BOOKING_CARD_SELECTOR = "[id^='booking-card-']"
CLASS_CARD_SELECTOR = "div[id^='class-card-']"

# -------------------------- Chrome Options ---------------------------- #
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile") 
chrome_options.add_argument(f"--user-data-dir={user_data_dir}") 

driver = webdriver.Chrome(options=chrome_options) 
driver.get(GYM_URL)
wait = WebDriverWait(driver, 10) 

# ------------------------------ Functions ------------------------------- #
def retry(func, retries=7): 
    for attempt in range(retries):
        try:
            return func() 
        except Exception as e:
            print(f"Attempt {attempt + 1} failed") 

            if attempt == retries - 1:
                raise e 

def book_class(button, class_name, day):
    if button.text == "Book Class":
        button.click()
        print(f"\n🎯 Booked: {class_name} on {day}")

    elif button.text == "Join Waitlist":
        button.click()
        print(f"\n🎯 Joined waitlist: {class_name} on {day}") 

def get_my_bookings():
    bookings = driver.find_elements(
        By.CSS_SELECTOR,
        BOOKING_CARD_SELECTOR    
    ) 
    print(f"\n📋 Total bookings found: {len(bookings)}\n")  
    return bookings     

def login():   
    login_button = wait.until(
        EC.presence_of_element_located(
            (By.ID, "login-button")
        )
    )
    login_button.click()

    email = wait.until(
        EC.presence_of_element_located(
            (By.ID, "email-input")
        )
    )
    password = wait.until(
        EC.presence_of_element_located(
            (By.ID, "password-input")
        )
    )

    email.click()
    email.send_keys(Keys.COMMAND, "a") 
    email.send_keys(Keys.BACKSPACE) 

    password.click()
    password.send_keys(Keys.COMMAND, "a")
    password.send_keys(Keys.BACKSPACE)

    email.send_keys(ACCOUNT_EMAIL)
    password.send_keys(ACCOUNT_PASSWORD)
    
    submit = wait.until(
        EC.presence_of_element_located(
            (By.ID, "submit-button")
        )
    )
    submit.click()

    class_schedule = wait.until(
        EC.presence_of_element_located(
            (By.ID, "schedule-link") 
        )
    )
    if class_schedule:
        print("\n✅ Successfully logged in!")

retry(login) 

# ----------------------------- Main Program ---------------------------- #

def main():
    class_cards = driver.find_elements(
        By.CSS_SELECTOR,
        CLASS_CARD_SELECTOR 
    )
    
    new_bookings = 0
    waitlists_joined = 0
    already_booked = 0
    already_waitlisted = 0
    total_processed = 0

    expected_thursday = None
    expected_tuesday = None

    for card in class_cards:
        parent = card.find_element(By.XPATH, "..")
        day_title = parent.find_element(By.TAG_NAME, "h2")
        day = day_title.text 

        time_element = card.find_element(
            By.CSS_SELECTOR, 
            "p[id^='class-time-']"  
        )
        time = time_element.text 

        if "Thu" in day and "6:00 PM" in time:
            expected_thursday = day.replace("Tomorrow (", "").replace(")", "")

        if "Tue" in day and "6:00 PM" in time:
            expected_tuesday = day.replace("Tomorrow (", "").replace(")", "")

        class_name = card.find_element(
        By.CSS_SELECTOR,
        "h3[id^='class-name-']"
        ).text

        button = card.find_element(By.TAG_NAME, "button")
        button_text = button.text 

        if ("Tue" in day or "Thu" in day) and "6:00 PM" in time:
            total_processed += 1
            if class_name in ALLOWED_CLASSES:

                if button_text == "Book Class":
                    retry(lambda: book_class(button, class_name, day))
                    new_bookings += 1 

                elif button_text == "Join Waitlist":
                    retry(lambda: book_class(button, class_name, day))
                    waitlists_joined += 1 

                elif button_text == "Booked":
                    already_booked += 1  
                    print(f"\n✅ Already booked: {class_name} on {day}") 

                elif button_text == "Waitlisted":
                    already_waitlisted += 1
                    print(f"\nAlready waitlisted: {class_name} on {day}")

    # ------------------------- Booking Summary ---------------------------- #
    print("\n📊 Booking Summary")
    print(f"New bookings: {new_bookings}")
    print(f"Waitlists joined: {waitlists_joined}")
    print(f"Already booked: {already_booked}")
    print(f"Already waitlisted: {already_waitlisted}")
    print(f"Total processed: {total_processed}")

    # ---------------------------- My Bookings ------------------------------ #
    wait.until(
        EC.presence_of_element_located(
            (By.ID, "my-bookings-link")
        )
    )
    driver.get("https://appbrewery.github.io/gym/my-bookings/")

    booking_page = wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "h1"),
            "My Bookings"
        )
    )
    if booking_page:
        print("\n✅ My Bookings page opened!")

    bookings = retry(get_my_bookings)  

    thursday_booked = False
    tuesday_booked = False

    for booking in bookings:

        if expected_thursday in booking.text and any(
                        allowed_class in booking.text 
                        for allowed_class in ALLOWED_CLASSES 
                        ):
            thursday_booked = True

        if expected_tuesday in booking.text and any(
                        allowed_class in booking.text 
                        for allowed_class in ALLOWED_CLASSES
                        ):
            tuesday_booked = True

        if "6:00 PM" in booking.text and ("Tue" in booking.text or "Thu" in booking.text): 
            print(booking.text)
            print("----------------")  

    # -------------------------- Booking Verification --------------------- #

    if thursday_booked:
        print(f"\n✅ Thursday 6 PM booking verified!")
    else:
        print(f"\n❌ Thursday 6 PM booking NOT found!")

    if tuesday_booked:
        print(f"\n✅ Tuesday 6 PM booking verified!")
    else:
        print(f"\n❌ Tuesday 6 PM booking NOT found!") 

if __name__ == "__main__":
    main() 