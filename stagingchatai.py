import json
from flask import Flask, jsonify
import string
import time
import random

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)
@app.route('/')
def index():
    try:
        service = Service(executable_path="C:\\Users\\\LENOVO\\Downloads\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        # driver = webdriver.Chrome(executable_path="C:\\Users\\\LENOVO\\Downloads\\chromedriver.exe")
        pswrd = "123456789"
        signup = "Sign-up Successfully"
        signin = "Sign-in Successfully"
        prompt1 = "My Chat GPT 3.5 prompt is 'What is the capital of punjab,pk?' &"
        options.add_argument("window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)

        import random

        # List of animal names
        animal_names = [
            "Elephant", "Tiger", "Lion", "Giraffe", "Zebra", "Hippopotamus", "Kangaroo",
            "Panda", "Koala", "Dolphin", "Whale", "Octopus", "Gorilla", "Penguin", "Ostrich",
            "Cheetah", "Leopard", "Rhinoceros", "Polar Bear", "Monkey", "Cat", "Dog", "Horse", "Shark"
        ]

        a = random_animal = random.choice(animal_names)
        print("Random Animal Name:", random_animal)


        driver.get("https://chatnowwithai.netlify.app/")
        time.sleep(2)
        driver.find_element(By.NAME, "search").send_keys("hi")
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(2)
        print("free prompt used")
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div/button[2]").click()
        time.sleep(5)
        driver.find_element(By.NAME, "first_name").send_keys("Testing")
        time.sleep(1)
        driver.find_element(By.NAME, "last_name").send_keys("VT")
        time.sleep(1)

        def generate_email():
            random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            email = f"{random_string}@sqa.com"
            return email

        print(generate_email())
        driver.find_element(By.NAME, "email").send_keys(generate_email())

        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("123456789")
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "account-button").click()
        time.sleep(3)
        print(signup)

        time.sleep(3)
        #signout
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div[3]/div[2]/button[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[3]/div/div[2]/div[4]/div/div/div/div/div/div/button[2]").click()
        time.sleep(2)
        # sign-in process
        driver.find_element(By.NAME, "email").send_keys("dirih49632@djpich.com")
        driver.find_element(By.NAME, "password").send_keys("112@Maher")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/form/button").click()
        time.sleep(2)
        print(signin)
        time.sleep(2)
        driver.get("https://ui.chatai.com/home")
        time.sleep(2)
        # remaining prompts
        pr = driver.find_element(By.XPATH,
                                 "/html/body/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div[1]/div[1]/div/p").text
        time.sleep(1)
        print(pr)
        time.sleep(3)
        driver.find_element(By.ID, "search").send_keys("What is the capital of punjab,pk?")
        time.sleep(3)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(5)
        print(prompt1)
        msggpt3 = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[3]/div[3]/div/div/div/p[2]").text
        time.sleep(2)
        # chat gpt 4.0
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/div/div[1]/p").click()
        time.sleep(1)
        driver.find_element(By.NAME, "search").send_keys("What is the capital of KPK,pk?")
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(8)
        gpt4 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div[3]/div/div/div/p[2]/p").text

        print("GPT 4.0")
        # Picasso
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[3]/div/div").click()
        driver.find_element(By.NAME, "search").send_keys(a)
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(10)
        img_element = driver.find_element(By.XPATH, "//img[@src='https://chatai-pub-dev.s3.eu-north-1.amazonaws.com/8bb3befb-64a9-48cb-925d-0c3d1b8131ac.png']")
        pcs = img_element.get_attribute("src")
        print(pcs)

        time.sleep(3)
        print(pcs)
        time.sleep(1)
        print("picasso working")
        # Ai2i
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[4]/div/div/div").click()
        driver.find_element(By.NAME, "search").send_keys("water formula")
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(10)
        ai2i = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div[3]/div/div").text
        time.sleep(3)
        print("Ai2i working")
        # Cohere
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[5]/div/div/div").click()
        driver.find_element(By.NAME, "search").send_keys("Restaurants in Lahore")
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(10)
        coh= driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div[3]/div/div/div").text
        time.sleep(2)
        print("cohere working")
        # Huggingface hub
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div/div[6]/div/div/div/div[1]").click()
        driver.find_element(By.NAME, "search").send_keys("Best night stay in hunza")
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER * 1)
        actions.perform()
        time.sleep(10)
        #hfh=driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/div[3]/div/div/div").text
        time.sleep(2)
        print("Huggingface hub working")

        # whatsapp message
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
        message = f"This is the email address {generate_email()}\n & this is the password {pswrd}\n, Remaining prompts are '{pr}'\n. {signup}\n, {signin}\n, {prompt1} the response is '{msggpt3}', For Picasso the animal name is '{a}' & Response is '{pcs}', Ai2i response is '{ai2i}', Cohere`s response is '{coh}."

        # Send email
        send_email(sender_email, sender_password, recipient_email, subject, message)
        return jsonify(Signup= signup, email= generate_email(), password=pswrd, Remaining_prompts= pr, signin= signin, My_prompt=prompt1, Response_from_chatgpt3=msggpt3, chatgpt4=gpt4, Ai2i=ai2i, picasso=pcs, Cohere=coh,) #Huggingfacehub=hfh)
    except Exception as e:
        print("An Exception occur")
        print(e)
        return jsonify({'error': "An Exception occur"})

app.run(host='0.0.0.0',port=3005)

