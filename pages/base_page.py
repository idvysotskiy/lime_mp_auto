# file: base_page.py
import time
from datetime import date
import allure
import re
from locators import *
from config import *
import random
import string
from uiautomator2 import Direction
import unittest
import uiautomator2 as u2


class InstallAPK:
    d = u2.connect(device_id)

    def clear_app_data(self):
        self.d.app_stop(package)
        self.d.app_clear(package)

    def install_app(self):
        self.d.app_install(app_link)

    def remove_app(self):
        self.d.app_uninstall(package)

    def stop_app(self):
        self.d.app_stop(package)


class BasePage:
    d = u2.connect(device_id)

    def swipe_page_down(self):
        self.d.swipe_ext(Direction.BACKWARD)

    def swipe_page_left(self):
        self.d.swipe_ext(Direction.HORIZ_FORWARD)

    def swipe_page_right(self):
        self.d.swipe_ext(Direction.HORIZ_BACKWARD)

    def swipe(self, swipe_ext):
        self.d.swipe_ext(swipe_ext, scale=0.8)

    def generate_random_email(self):
        domain = "@yandex.ru"
        username_length = random.randint(5, 10)
        rnd_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
        username = 'lime.tester+'
        return username + rnd_name + domain

    def get_element_text(self, locator, element_name):
        element = self.d.xpath(locator)
        element.wait(timeout=10)
        assert element.exists, f"Catalog item '{element_name}' not found"
        print(element.get_text())

    def is_element_present(self, locator):
        unittest.TestCase.assertTrue(self.d.xpath(locator).exists, 'Element not found!')

    def cancel_notification(self):
        element = self.d.xpath(MainLocators.NOTIFICATION_NEGATIVE).wait(timeout=10)
        if element is not None:
            self.d.xpath(MainLocators.NOTIFICATION_NEGATIVE).click()

    def test_text(self, locator, text):
        assert self.d.xpath(locator).get_text() == text

    def current_date(self):
        current_date = date.today()
        return current_date

    def get_screen(self):
        # print('screen')
        screen = "screen.png"
        self.d.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)

    def click(self, locator, element_name=None):
        if element_name is not None:
            with allure.step("Клик по элементу '{element_name}'"):
                if isinstance(locator, str):
                    self.get_element(locator).click()
                else:
                    locator.click()
        else:
            if isinstance(locator, str):
                self.get_element(locator).click()
            else:
                locator.click()

    def set_text(self, locator, text, element_name=None):
        if element_name is not None:
            with allure.step("Заполнение поля '{element_name}' текстом '{text}'"):
                self.get_element(locator).set_text(text)
        else:
            self.get_element(locator).set_text(text)

    def get_element(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            return self.d.xpath(locator)
        else:
            return self.d(resourceId=locator)

    def get_text(self, locator):
        return self.get_element(locator).get_text()

    def wait_a_moment(self):
        time.sleep(0.5)

    def wait_a_second(self):
        time.sleep(1)

    def swipe_page_up(self, count=None):
        if count is not None:
            for i in range(count):
                self.d.swipe_ext(Direction.FORWARD)
        else:
            self.d.swipe_ext(Direction.FORWARD)

    def swipe_down(self):
        self.d.swipe(400, self.d.window_size()[1] / 2, 400, self.d.window_size()[1] / 4)

    @allure.step('Сделать свайп влево')
    def swipe(self, swipe_ext):
        self.d.swipe_ext(swipe_ext, scale=0.8)

    def clear_text(self, locator, element_name=None):
        if element_name is not None:
            with allure.step("Удалить текст из поля '{element_name}'"):
                self.get_element(locator).click()
        else:
            self.d.clear_text()

    def get_random_element(self, locator):
        if isinstance(locator, str):
            if locator[0] == '/' and locator[1] == '/':
                counter = random.randrange(0, len(self.d.xpath(locator).all()))
                elements_list = self.d.xpath(locator).all()
                return elements_list[counter]
            else:
                counter = random.randrange(0, self.d(resourceId=locator).count)
                return self.d(resourceId=locator)[counter]
        else:
            counter = random.randrange(0, locator.count)
            return locator[counter]

    def wait_element(self, locator, element_name=None):
        # time.sleep(5)
        if element_name is not None:
            with allure.step(f"Ожидание элемента '{element_name}'"):
                if isinstance(locator, str):
                    if locator[0] == '/' and locator[1] == '/':
                        assert self.get_element(locator).exists == True, print(f"Элемент {element_name} отсутствует")
                    else:
                        assert self.get_element(locator).wait(10) == True, print(f"Элемент {element_name} отсутствует")
                else:
                    assert locator.wait(10) == True, print(f"Элемент {element_name} отсутствует")
        else:
            if isinstance(locator, str):
                if locator[0] == '/' and locator[1] == '/':
                    assert self.get_element(locator).exists == True
                else:
                    assert self.get_element(locator).wait(10) == True
            else:
                assert locator.wait(10) == True

    def wait_text(self, text):
        assert self.d(text=text).wait(10) == True, print(f"Элемент с текстом '{text}' не найден")

    def close_popup(self):
        self.d.click(0.477, 0.031)

    def get_number_from_element(self, element):
        return int(re.sub('[^0-9]', "", self.get_text(element)))
