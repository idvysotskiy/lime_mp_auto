# file: base_page.py
import time

import allure

from locators import *
from config import *
import random
import string
from uiautomator2 import Direction


class InstallAPK:
    def __init__(self, device):
        self.device = device

    def clear_app_data(self):
        self.device.app_stop(package)
        self.device.app_clear(package)

    def install_app(self):
        self.device.app_install(app_link)

    def remove_app(self):
        self.device.app_uninstall(package)

    def stop_app(self):
        self.device.app_stop(package)


class BasePage:
    def __init__(self, device):
        self.device = device

    # def find_element_by_text(self, element_text):
    # self.device.xpath(//*[@text=element_text])
    def swipe_page_up(self):
        self.device.swipe_ext(Direction.FORWARD)

    def swipe_page_down(self):
        self.device.swipe_ext(Direction.BACKWARD)

    def swipe_page_left(self):
        self.device.swipe_ext(Direction.HORIZ_FORWARD)

    def swipe_page_right(self):
        self.device.swipe_ext(Direction.HORIZ_BACKWARD)

    def swipe(self, swipe_ext):
        self.device.swipe_ext(swipe_ext, scale=0.8)


    def generate_random_email(self):
        domain = "@example.com"
        username_length = random.randint(5, 10)
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
        return username + domain

    def get_element_text(self, locator, element_name):
        element = self.device.xpath(locator, text=element_name)
        element.wait(timeout=10)
        assert element.exists, f"Catalog item '{element_name}' not found"
        print(element.get_text())

    def is_element_present(self, locator):
        assert self.device.xpath(locator).exists == True, 'Element not found!'

    def cancel_notification(self):
        element = self.device.xpath(MainLocators.NOTIFICATION_NEGATIVE).wait(timeout=10)
        if element is not None:
            self.device.xpath(MainLocators.NOTIFICATION_NEGATIVE).click()

    def test_text(self, locator, text):
        assert self.device.xpath(locator).get_text() == text

    def get_screen(self):
        screen = "screen.png"
        self.device.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)


    def current_date(self):
        current_date = date.today()
        return current_date

    def generate_random_email(self):
        domain = "@yandex.ru"
        username_length = random.randint(5, 10)
        rnd_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
        username = 'yapmap.tester+'
        return username + rnd_name + domain

    def is_element_present(self, locator):
        print(self.device.xpath(locator).exists)
        assert self.device.xpath(locator).exists == True, 'Element not found!'

    def get_screen(self):
        print('screen')
        # screen = "screen.png"
        # self.d.screenshot(screen)
        # allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)

    def click(self, locator, element_name=None):
        if element_name is not None:
            with allure.step("Клик по элементу '{element_name}'"):
                self.get_element(locator).click()
        else:
            self.get_element(locator).click()

    def set_text(self, locator, text, element_name=None):
        if element_name is not None:
            with allure.step("Заполнение поля '{element_name}' текстом '{text}'"):
                self.get_element(locator).set_text(text)
        else:
            self.get_element(locator).set_text(text)

    def get_element(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            return self.device.xpath(locator)
        else:
            return self.device(resourceId=locator)

    def get_text(self, locator):
        return self.get_element(locator).get_text()

    def wait_a_moment(self):
        time.sleep(0.5)

    def wait_a_second(self):
        time.sleep(1)

    def swipe_down(self):
        self.device.swipe(400, self.device.window_size()[1] / 2, 400, self.device.window_size()[1] / 4)

    @allure.step('Сделать свайп влево')
    def swipe(self, swipe_ext):
        self.device.swipe_ext(swipe_ext, scale=0.8)

    # @allure.step('Сделать свайп вверх')
    # def swipe_page(self):
    #     self.d.swipe_ext(Direction.HORIZ_FORWARD)

    def clear_text(self, locator, element_name=None):
        if element_name is not None:
            with allure.step("Удалить текст из поля '{element_name}'"):
                self.get_element(locator).click()
        else:
            self.device.clear_text()


