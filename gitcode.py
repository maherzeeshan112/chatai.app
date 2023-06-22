import string
import time
import random

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver

from selenium.webdriver import ActionChains, ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import headless

service = Service(executable_path="C:\\Users\\\LENOVO\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
#driver = webdriver.Chrome(executable_path="C:\\Users\\\LENOVO\\Downloads\\chromedriver.exe")
print(type(driver))
pswrd = "123456789"
signup = "Sign-up Successfully"
signin = "Sign-in Successfully"
prompt1 = "Chat GPT 3.5 Prompt, My prompt is 'What is the capital of punjab,pk?' &"
driver.implicitly_wait(10)
webdriver.chrome(headless)
driver.maximize_window()

driver.get("https://wp.chatai.com/")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[1]/div/a[1]/img").click()
time.sleep(2)
driver.find_element(By.NAME, "search").send_keys("hi")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(5)
driver.find_element(By.NAME, "search").send_keys("hi")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(5)
driver.find_element(By.NAME, "search").send_keys("hi")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(5)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div/button[2]").click()
time.sleep(3)
driver.find_element(By.NAME, "first_name").send_keys("Testing")
time.sleep(1)
driver.find_element(By.NAME, "last_name").send_keys("VT")
time.sleep(1)
def generate_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{random_string}@example.com"
    return email
print(generate_email())
driver.find_element(By.NAME, "email").send_keys(generate_email())

time.sleep(1)
driver.find_element(By.NAME, "password").send_keys("123456789")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "account-button").click()
time.sleep(3)
print(signup)
#remaining prompts
pr = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/p").text
time.sleep(1)
print(pr)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/button[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div[3]/div/div/div/div/div/div/button[2]").click()
time.sleep(2)
#sign-in process
driver.find_element(By.NAME, "email").send_keys("dirih49632@djpich.com")
driver.find_element(By.NAME, "password").send_keys("112@Maher")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/form/button").click()
time.sleep(2)
print(signin)
driver.find_element(By.NAME, "search").send_keys("What is the capital of punjab,pk?")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(5)
print(prompt1)
msg = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[3]/div[4]/div/div/div/p[2]/p").text
time.sleep(2)
#chat gpt 4.0
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/div/div[1]/p").click()
time.sleep(1)
driver.find_element(By.NAME, "search").send_keys("What is the capital of KPK,pk?")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(5)
#Picasso
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[3]/div/div").click()
driver.find_element(By.NAME, "search").send_keys("Cat")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(10)
#Ai2i
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[4]/div/div/div").click()
driver.find_element(By.NAME, "search").send_keys("water formula")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(10)

#Cohere
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[5]/div/div/div").click()
driver.find_element(By.NAME, "search").send_keys("Restaurants in Lahore")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(10)

#Huggingface hub
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[6]/div/div/div/div[1]").click()
driver.find_element(By.NAME, "search").send_keys("Best night stay in hunza")
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER * 1)
actions.perform()
time.sleep(10)

#whatsapp message
# driver.get("https://wp.chatai.com/")
# driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[1]/div/a[2]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a/span")



def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Add body to email
    msg.attach(MIMEText(message, "plain"))

    try:
        # Create SMTP session
        smtp = smtplib.SMTP("smtp.gmail.com", 587)

        # Start TLS for security
        smtp.starttls()

        # Login to the sender's email account
        smtp.login(sender_email, sender_password)

        # Send email
        smtp.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        print(e)
    finally:
        # Terminate the SMTP session
        smtp.quit()

# Sender's credentials
sender_email = "zrafique789@gmail.com"
sender_password = "pwpfajnzearhtehr"

# Recipient's email
recipient_email = "zeshan146@gmail.com"

# Email content
subject = "Test Automation Completed and result is in Body"
message = f"This is the email address {generate_email()} & this is the password {pswrd}, Remaining prompts are '{pr}'. {signup}, {signin}, {prompt1} the response is '{msg}'. "

# Send email
send_email(sender_email, sender_password, recipient_email, subject, message)
