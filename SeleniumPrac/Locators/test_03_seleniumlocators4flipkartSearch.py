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

@allure.title("flipkart positive test case for search results")
@allure.description("TC! on flipkart search results")

def test_flipkart_seasrchResults():
    driver = webdriver.Chrome()
    URL = driver.get("https://www.flipkart.com")

#find element search
#    < input    class ="lNPl8b" type="text" title="Search for Products, Brands and More" name="q" autocomplete="off" placeholder="Search for Products, Brands and More" value="" >
    search = driver.find_element(By.CLASS_NAME,value="lNPl8b")
    time.sleep(5)
    search.send_keys("macbook")

#mouse hovering to particular result and click on
    #< div class ="RG5Slk" > Apple MacBook Pro M3 Pro - (18 GB / 1 TB SSD / macOS Sonoma) MRX43HN / A < / div >
    search_results = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//li[4]")))
    ActionChains(driver).move_to_element(search_results).click().perform()

#selecting search results with user specifications
    macbook_pro = driver.find_element(By.XPATH,"//div[@class='RG5Slk' and contains(text(),'Apple MacBook Pro M5 - (16 GB/512 GB SSD/macOS Tahoe) MDE44HN/A')]")
    macbook_pro.click()

#checking URL for user item
    check_url = driver.current_url
    if(URL!=check_url):
        print("URL has changed")