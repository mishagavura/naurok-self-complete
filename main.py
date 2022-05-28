from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from answers import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")


driver = webdriver.Chrome(executable_path="driver/chromedriver", options=chrome_options )

driver.get("https://naurok.com.ua/test/testing/aa7c6273-a0ec-406a-9067-f1bc40de7a0f")
test_is_compelete = False
while not test_is_compelete:
    time.sleep(3)
    question_test = driver.find_element(By.CLASS_NAME, "test-content-text-inner").text
    for item in answers_json:
        if question_test.replace('&nbsp;', ' ').strip() == item['question'].replace('</em>', '').replace('<em>', '').replace('<strong>', '').replace('</strong>', '').replace('&nbsp;', ' ').strip():
            answers_button_arr = driver.find_elements(By.CLASS_NAME, "question-option-inner-content")
            for elem in answers_button_arr:
                if elem.text.strip() == item['answer'].replace('</em>', '').replace('<em>', '').replace('&nbsp;', ' ').strip():
                    elem.click()
    time.sleep(2)
    try:
        submit_button = driver.find_element(By.CLASS_NAME, "test-multiquiz-save-button")
        submit_button.click()
    except NoSuchElementException:
        pass
   


