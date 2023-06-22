from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

# Generate a random email address
def generate_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{random_string}@example.com"
    return email

email_input = driver.find_element_by_id("email")  # Replace with the actual ID of the email input field
email_input.clear()
email_input.send_keys(generate_email())

# Submit the form
submit_button = driver.find_element_by_id("submit")  # Replace with the actual ID of the submit button
submit_button.click()

# Close the browser
driver.quit()