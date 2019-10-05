import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",\
                                  #"https://stepik.org/lesson/236896/step/1",\
                                  #"https://stepik.org/lesson/236897/step/1",\
                                  #"https://stepik.org/lesson/236898/step/1",\
                                  #"https://stepik.org/lesson/236899/step/1",\
                                  #"https://stepik.org/lesson/236903/step/1",\
                                  #"https://stepik.org/lesson/236904/step/1",\
                                  #"https://stepik.org/lesson/236905/step/1"
                                ])
def test_guest_should_see_login_link(browser, link):
    link = f"{link}"
    browser.get(link)

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "textarea.ember-text-area.ember-view")))

    answer = math.log(int(time.time()))

    input_field = browser.find_element_by_class_name("textarea.ember-text-area.ember-view")
    input_field.send_keys(answer)

    submit_button = browser.find_element_by_class_name("submit-submission ")
    submit_button.click()

    final_text = browser.find_element_by_class_name("smart-hints__hint")

    print(final_text)







