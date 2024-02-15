# file: base_page.py
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
        assert self.device.xpath(locator).exists, 'Element not found!'

    def cancel_notification(self):
        element_is_present = self.device.xpath(MainLocators.NOTIFICATION_NEGATIVE).wait(timeout=10)
        if element_is_present is not None:
            self.device.xpath(MainLocators.NOTIFICATION_NEGATIVE).click()

    def test_text(self, locator, text):
        assert self.device.xpath(locator).get_text() == text

    def get_screen(self):
        screen = "screen.png"
        self.device.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)


