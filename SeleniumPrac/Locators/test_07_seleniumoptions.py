import time
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@allure.title("Open the app.vwo.com")
@pytest.mark.regression

def test_katalon():
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options)
    #using Chrome-options - headless provide a mode of automating test case without looking into UI and also it has features like maximise with customise resolution
    chrome_options.add_argument("--headless")
    #<a id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">Make Appointment</a>
    #1 this code is translated into the API request
    #2. POST request - browserDriver(server)
    #3 Where it will create session or fresh copy browser(Chrome)
    #4 Session id - 16 digit (t21785872376369829713) will be
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment = driver.find_element(By.ID, value="btn-make-appointment")
    make_appointment.click()
    #Verifying the URL after clicking
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(15)
    driver.quit()