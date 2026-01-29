import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("TC for lists")
@allure.description("Positive test case for printing the details of item in ebay platform")

def test_ebay():
    driver = webdriver.Chrome()
    ebay_Web = driver.get("https://www.ebay.com")
    time.sleep(5)
    search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='gh-ac']")))
    search.click()
    search_macmini = search.send_keys("Mac mini")
    time.sleep(5)
    search_btn = driver.find_element(By.XPATH,"//button[@id='gh-search-btn']").click()
    time.sleep(5)
    #getting details about the searched item which displayed on the front page
    searched_macmini_dtls = driver.find_elements(By.XPATH,"//ul[@class='srp-results srp-list clearfix']//li")
    for info in searched_macmini_dtls:
        print(info.text)

