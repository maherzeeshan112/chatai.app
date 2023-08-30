import json
from flask import Flask, jsonify
import pyperclip
import time
import re
import pyautogui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service(executable_path="C:\\Users\\\LENOVO\\Downloads\\geckodriver.exe")
options = webdriver.FirefoxOptions()


#options.add_argument("--headless")
 # driver = webdriver.Chrome(executable_path="C:\\Users\\\LENOVO\\Downloads\\chromedriver.exe")
pswrd = "123456789"

prompt1 = "My Chat GPT 3.5 prompt is 'What is the capital of punjab,pk?"
options.add_argument("window-size=1920,1080")

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(10)

driver.get("http://staging.lastingsales.com")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[1]/div[2]/form/div[1]/div/input").send_keys("qatesting@yopmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[1]/div[2]/form/div[2]/div/input").send_keys("Admin@123")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[1]/div[2]/form/button").click()
time.sleep(3)
pyautogui.click(520, 160)

