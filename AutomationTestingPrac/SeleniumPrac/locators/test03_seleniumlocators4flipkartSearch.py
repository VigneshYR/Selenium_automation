import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("VMO login negative test cases app.vwo.com")
@allure.description("VMO TC! negative TC - VMO login with invalid creditials")

def test_vwo_login():
    driver = webdriver.Safari()
    URL = driver.get("https://www.flipkart.com")

#find element search
#    < input    class ="lNPl8b" type="text" title="Search for Products, Brands and More" name="q" autocomplete="off" placeholder="Search for Products, Brands and More" value="" >
    search = driver.find_element(By.CLASS_NAME,value="lNPl8b")
    time.sleep(5)
    search.send_keys("mac")

#mouse hovering to particular result and click on
    #< div class ="RG5Slk" > Apple MacBook Pro M3 Pro - (18 GB / 1 TB SSD / macOS Sonoma) MRX43HN / A < / div >
    search_results = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='URRkKz RzamwD']")))
    ActionChains(driver).move_to_element(search_results).click().perform()