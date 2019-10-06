import time
import math
import pytest


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
    answer = math.log(int(time.time()))

    browser.implicitly_wait(15)

    input_field = browser.find_element_by_class_name("textarea.ember-text-area.ember-view")
    input_field.send_keys(str(answer))

    submit_button = browser.find_element_by_class_name("submit-submission ")
    submit_button.click()

    browser.implicitly_wait(15)

    final_text = browser.find_element_by_class_name("smart-hints__hint").text

    assert final_text == "Correct!", "Текст не соответствует ожидаемому!"

    print(final_text)







