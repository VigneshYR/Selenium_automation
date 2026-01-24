import time
from selenium import webdriver
import allure
import pytest

@allure.title("Open the app.vwo.com")
@pytest.mark.regression

def test_vwo_login():
    driver = webdriver.Chrome()
    #1 this code is translated into the API request
    #2. POST request - browserDriver(server)
    #3 Where it will create session or fresh copy browser(Chrome)
    
    driver.get("https://app.vmo.com")
    time.sleep(15)