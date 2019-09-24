from selenium import webdriver
import time
import unittest


class Test_Registration(unittest.TestCase):
    def test_registration1(self):

        link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_css_selector("input.form-control.first[required]")
        input1.send_keys("required1")

        input2 = self.browser.find_element_by_css_selector("input.form-control.second[required]")
        input2.send_keys("required2")

        input3 = self.browser.find_element_by_css_selector("input.form-control.third[required]")
        input3.send_keys("required3")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = self.browser.find_element_by_tag_name("h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def test_registration2(self):

        link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_css_selector("input.form-control.first[required]")
        input1.send_keys("required1")

        input2 = self.browser.find_element_by_css_selector("input.form-control.second[required]")
        input2.send_keys("required2")

        input3 = self.browser.find_element_by_css_selector("input.form-control.third[required]")
        input3.send_keys("required3")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = self.browser.find_element_by_tag_name("h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()