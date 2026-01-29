import time
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By

@allure.title("Make an appointment")
@allure.description("Go through the katalon website and make an appointment")
@pytest.mark.positive

def test_katalon_makeAppointment():
    driver = webdriver.Chrome()
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