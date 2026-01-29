import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("positive test case error message")
@allure.description("positive test case for checking error message while login with invalid credintials")
def test_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    links = driver.find_elements(By.TAG_NAME,"a")
    print(len(links))
    for i in links:
        time.sleep(5)
        print(i.text)
    link_free_trial = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")