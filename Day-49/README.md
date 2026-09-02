# 🏋️ Gym Class Booking Automation

A Selenium WebDriver automation project built as part of my **100 Days of Python** learning journey.

This project automates gym class bookings on a **simulated gym website provided by the course**.

## ✨ Features

- Automated student login
- Finds Tuesday and Thursday 6:00 PM classes
- Supports Yoga, Spin, and HIIT classes
- Books available classes
- Joins the waitlist when a class is full
- Detects already booked and waitlisted classes
- Retries failed operations caused by simulated network failures
- Displays a booking summary
- Verifies bookings on the My Bookings page
- Tested with different simulated dates

## 🛠️ Technologies

- Python
- Selenium WebDriver
- Google Chrome

## 🧠 Concepts Practiced

- Selenium WebDriver
- Explicit waits with `WebDriverWait`
- Expected Conditions
- CSS Selectors
- XPath
- Functions
- Lambda functions
- Exception handling
- Custom retry logic
- Dynamic date handling
- Web element interaction
- Booking verification

## 🔄 Retry Mechanism

The course website includes a **network simulation** feature that intentionally causes some operations to fail.

To handle these failures, I implemented a custom retry function that attempts an operation up to **7 times**.

Example:

```text
Attempt 1 failed
Attempt 2 failed
Attempt 3 failed
Attempt 4 failed
Attempt 5 failed
Attempt 6 failed

Successfully logged in!
```

## 📊 Example Output

```text
Attempt 1 failed
Attempt 2 failed
Attempt 3 failed
Attempt 4 failed
Attempt 5 failed
Attempt 6 failed

✅ Successfully logged in!

✅ Already booked: Spin Class on Tue, Sep 8

🎯 Booked: Spin Class on Thu, Sep 10

📊 Booking Summary
New bookings: 1
Waitlists joined: 0
Already booked: 1
Already waitlisted: 0
Total processed: 2

✅ My Bookings page opened!

📋 Total bookings found: 110

Spin Class
When: Tue, Sep 8, 6:00 PM
Instructor: Carlos Rodriguez
Duration: 45 minutes
Cancel Booking
----------------
Spin Class
When: Tue, Sep 22, 6:00 PM
Instructor: Carlos Rodriguez
Duration: 45 minutes
Cancel Booking
----------------
Spin Class
When: Thu, Sep 24, 6:00 PM
Instructor: Mike Johnson
Duration: 45 minutes
Cancel Booking
----------------
Spin Class
When: Thu, Oct 1, 6:00 PM
Instructor: Mike Johnson
Duration: 45 minutes
Cancel Booking
----------------
Spin Class
When: Thu, Oct 8, 6:00 PM
Instructor: Mike Johnson
Duration: 45 minutes
Cancel Booking
----------------

✅ Thursday 6 PM booking verified!

✅ Tuesday 6 PM booking verified!
```

## 🧪 Testing

The automation was tested using the course website's **network simulation** feature to verify that the retry mechanism could handle failed operations.

I also advanced the website's **simulated date** during testing to make sure the automation could work with changing dates instead of relying on hardcoded dates.

## ⚠️ Note

This project uses a **simulated gym website provided by the course** for educational and testing purposes.

It does not interact with a real gym or real booking system.

## 🎯 Learning Outcome

This project helped me practice building a complete Selenium automation workflow — from logging in and finding the required classes to handling different booking states, recovering from simulated failures, and verifying the final results.