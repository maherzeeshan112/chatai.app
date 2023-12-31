import pyperclip
from flask import Flask, jsonify
import time
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

app = Flask(__name__)
@app.route('/')
def index():
    try:

        service = Service(executable_path="C:\\Users\\\LENOVO\\Downloads\\geckodriver.exe")
        options = webdriver.FirefoxOptions()


        #options.add_argument("--headless")
        pswrd = "123456789"

        options.add_argument("window-size=1920,1080")

        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.implicitly_wait(15)

        import random

        # List of animal names
        animal_names = [
            "Elephant", "Tiger", "Lion", "Giraffe", "Zebra", "Hippopotamus", "Kangaroo",
            "Panda", "Koala", "Dolphin", "Whale", "Octopus", "Gorilla", "Penguin", "Ostrich",
            "Cheetah", "Leopard", "Rhinoceros", "Polar Bear", "Monkey", "Cat", "Dog", "Horse", "Shark"
        ]

        a = random_animal = random.choice(animal_names)
        print("Picasso Prompts is:", random_animal)

        driver.get('https://www.guerrillamail.com/inbox')
        email = driver.find_element(By.ID, "email-widget").text
        time.sleep(2)

        # Use the copied value
        print(email)

        driver.execute_script("window.open('about:blank', '_blank');")

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[1])

        driver.get("https://wp.chatai.com/")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[1]/div/a[1]/img").click()

        time.sleep(5)
        driver.find_element(By.ID, "sign-up-first_name").send_keys("Testing")
        time.sleep(1)
        driver.find_element(By.ID, "sign-up-last_name").send_keys("Bot Python")
        time.sleep(1)

        driver.find_element(By.ID, "sign-up-email").send_keys(email)

        time.sleep(1)
        driver.find_element(By.ID, "sign-up-password").send_keys("123456789")
        time.sleep(1)

        try:

            driver.find_element(By.ID, "sign-up-btn").click()
            time.sleep(5)
           # driver.switch_to.window(driver.window_handles[0])
            #time.sleep(25)

            # Refresh the email inbox
            #driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div[2]/form/table/tbody/tr[1]/td[3]').click()

            # Wait for the email to appear
            #time.sleep(5)
            #text_with_numbers = driver.find_element(By.XPATH,
             #                                       "/html/body/div[4]/div/div[3]/div[2]/div/div/div[2]/div/center/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/div/div[1]/p").text
            #otp = re.findall(r'\d+', text_with_numbers)
            #print('Numbers found:', otp)

            #time.sleep(2)
            #driver.switch_to.window(driver.window_handles[1])
            #time.sleep(2)
            #driver.find_element(By.ID, "otp").send_keys(otp)
            #time.sleep(2)

            #driver.find_element(By.ID, "otp-btn").click()
            #print("otp accepted")

            signup = "Sign-up Successfully"
            print("Sign-up Successfully")
        except NoSuchElementException:
            print("Sign-up is Not Working")
            signup = "Sign-up is Not Working"

            time.sleep(4)

        #signout
        driver.find_element(By.ID, "logout").click()
        time.sleep(3)
        driver.find_element(By.ID, "confirm").click()
        time.sleep(2)
        # sign-in process
        driver.find_element(By.ID, "sign-in-email").send_keys(email)
        driver.find_element(By.ID, "sign-in-password").send_keys("123456789")
        time.sleep(1)

        try:

            driver.find_element(By.ID, "sign-in-btn").click()
            time.sleep(2)


            signin= "Sign-in Successfully"
            print("Sign-in Successfully")

        except NoSuchElementException:
            print("Sign-in is not working")
            signin = "Sign-in is not working"
        time.sleep(3)


        time.sleep(2)
        driver.get("https://ui.chatai.com/home")
        time.sleep(3)
        # remaining prompts
        pr = driver.find_element(By.ID,"remaining-prompts").text
        time.sleep(1)
        print(pr)
        time.sleep(3)
        driver.find_element(By.ID, "search").send_keys("What is the capital of punjab,pk?")
        time.sleep(3)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(5)
        try:

            msggpt3 = driver.find_element(By.XPATH,
                                          "/html/body/div/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div/div/div/p[2]").text

            print("GPT 3.5 is Working")

        except NoSuchElementException:
            print("GPT 3.5 is Not Working")
            msggpt3 = "Chat GPT 3.5 is Not Working, Looks like the model is down"


        time.sleep(2)
        # chat gpt 4.0
        driver.find_element(By.ID, "22G1").click()
        time.sleep(1)
        driver.find_element(By.NAME, "search").send_keys("What is the capital of KPK,pk?")
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(8)
        try:

            gpt4 = driver.find_element(By.XPATH,
                                       "/html/body/div/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div/div/div/p[2]/p").text

            print("GPT 4.0 is Working")

        except NoSuchElementException:
            print("GPT 4.0 is Not Working")
            gpt4 = "Chat GPT 4.0 is Not Working, Looks like the model is down"
        time.sleep(3)

        # Picasso
        driver.find_element(By.ID, "2A31").click()
        driver.find_element(By.NAME, "search").send_keys(a)
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(10)

        try:

            element = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div/div/div/p[2]")




            hidden_text = driver.execute_script("return arguments[0].textContent;", element)

            print(hidden_text)
            pcs = hidden_text
            print("picasso is working")
        except NoSuchElementException:
            print("Picasso is not Working")
            pcs = "Picasso Not Working, Looks like the model is down"
        time.sleep(3)

        # Ai2i
        driver.find_element(By.ID, "2DK1").click()
        driver.find_element(By.NAME, "search").send_keys("water formula")
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(10)
        try:

            ai2i = driver.find_element(By.XPATH,
                                       "/html/body/div/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div/div/div").text
            print("Ai2i is working")
        except NoSuchElementException:
            print("Ai2i is Not Working")
            ai2i = "Ai2i is Not Working, Looks like the model is down"

        time.sleep(3)

        # Cohere
        driver.find_element(By.ID, "2881").click()
        driver.find_element(By.NAME, "search").send_keys("Five steps to start driving a car")
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(10)
        try:

            coh = driver.find_element(By.XPATH,
                                      "/html/body/div/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div/div/div").text
            print("Cohere working")
        except NoSuchElementException:
            print("Cohere is Not Working")
            coh = "Cohere is Not Working, Looks like the model is down"

        time.sleep(2)

        # Huggingface hub
        driver.find_element(By.ID, "2ZQ1").click()
        driver.find_element(By.NAME, "search").send_keys("Best night stay in hunza")
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(10)
        try:

            hfh = driver.find_element(By.XPATH,
                                      "/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div[3]/div/div/div").text

            print("HuggingFace Hub is Working")

        except NoSuchElementException:
            print("HuggingFace Hub is Not Working")
            hfh = "HuggingFace Hub will launch soon, This model is still in development process"


        time.sleep(2)
        00
        pr2 = driver.find_element(By.ID,"remaining-prompts").text
        time.sleep(1)
        print(pr2)


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
        sender_email = "testbotforpython112@gmail.com"
        sender_password = "uayyndxyallcivne"

        # Recipient's email
        recipient_email = "zeshan146@gmail.com"

        # Email content
        subject = "Test Automation Completed and result is in Body"
        message = f"This is the email address {email}\n & this is the password {pswrd}\n, Remaining prompts are '{pr}'\n.{signup}\n, {signin}\n, The response from CHATGPT 3.5 is '{msggpt3}'\n, Chat GPT4.0 response is {gpt4},  For Picasso the animal name is '{a}' & Response is '{pcs}'\n, Ai2i response is '{ai2i}'\n, Cohere`s response is '{coh}. Hugging face hub response is '{hfh}'."

        # Send email
        send_email(sender_email, sender_password, recipient_email, subject, message)
        return jsonify(Signup=signup, email=email, password=pswrd, Remaining_prompts= pr, signin=signin,
                       Response_from_chatgpt3=msggpt3, chatgpt4=gpt4, picasso=pcs, Ai2i=ai2i, Cohere=coh,
                       Huggingfacehub=hfh, pr2=pr2)
    except Exception as e:
        print("An Exception occur")
        print(e)
        return jsonify({'error': "An Exception occur"})

app.run(host='0.0.0.0',port=5003)

