from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)


# required user input

selected_time = "9:30"

#choose between classes 'bjj' or 'nogi'
type_of_class = "bjj"

yourName = "test user"

#
#
#

driver.get("http://onetobjj.at")
results = driver.find_elements_by_class_name("time")
for result in results:
    if (result.text == selected_time):
        parent_element = result.find_element_by_xpath('..')
        gym_class = parent_element.find_element_by_class_name(type_of_class)

gym_class.click()

forminput = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ant-input'))
    )

forminput.click()
forminput.send_keys(yourName)

submit_button = driver.find_element_by_class_name("ant-btn-primary")
submit_button.click()

modal = driver.find_element_by_class_name("ant-modal-content")
modal.screenshot('confirm_booking.png')
        
