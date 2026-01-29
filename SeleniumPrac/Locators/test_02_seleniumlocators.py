import os
import time

from dotenv import load_dotenv
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@allure.title("VMO login negative test cases app.vwo.com")
@allure.description("VMO TC! negative TC - VMO login with invalid creditials")

def test_vwo_login():
    driver = webdriver.Firefox()
    URL=driver.get("https://app.vwo.com/")

#find email textfield
#input type="email" class="text-input W(100%)" name="username" vwo-html-translate-attr="placeholder" vwo-html-translate-placeholder="login:enterEmailID" id="login-username" data-qa="hocewoqisi" placeholder="Enter email ID">
    time.sleep(10)
    username_textfield = driver.find_element(By.ID,value="login-username")
    username_textfield.send_keys("vignesh")

#find element password text field
#< input type = "password" class ="text-input W(100%)" vwo-html-translate-attr="placeholder" vwo-html-translate-placeholder="login:enterPassword" name="password" id="login-password" data-qa="jobodapuxe" placeholder="Enter password" >
    password_textfield = driver.find_element(By.ID, value="login-password")
    password_textfield.send_keys("Vignesh")

#find element sign in button
    #< button type = "submit" id = "js-login-btn"
    sign_in = driver.find_element(By.ID, value="js-login-btn")
    time.sleep(10)
    sign_in.click()

# check the error message for Invalid username password
# <div class="notification-box-description" id="js-notification-box-msg"
    message_print = driver.find_element(By.ID, value="js-notification-box-msg")
    a = message_print.text
    print(a)

#compare URL after signin
    if(URL == driver.current_url):
        print("test case failed")

