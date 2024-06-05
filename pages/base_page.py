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
from PIL import Image


class BasePage:
    def __init__(self, d):
        self.d = d

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

    def get_element_text(self, locator: object, element_name: object) -> object:
        element = self.d.xpath(locator)
        element.wait(timeout=10)
        assert element.exists, f"Catalog item '{element_name}' not found"
        print(element.get_text())

    def is_element_present(self, locator):
        d = self.d
        unittest.TestCase.assertTrue(d.xpath(locator).exists, 'Element not found!')

    def cancel_notification(self):
        d = self.d
        element = d.xpath(MainLocators.NOTIFICATION_NEGATIVE).wait(timeout=10)
        if element is not None:
            d.xpath(MainLocators.NOTIFICATION_NEGATIVE).click()

    def test_text(self, locator, text):
        d = self.d
        assert d.xpath(locator).get_text() == text

    def current_date(self):
        current_date = date.today()
        return current_date

    def get_screen(self):
        screen = "screen.png"
        self.d.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)

    def click(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Клик по элементу '{element_name}'"):
                if isinstance(locator, str):
                    self.get_element(locator).click()
                    self.wait_a_moment()
                    self.get_screen()
                else:
                    locator.click()
                    self.wait_a_moment()
                    self.get_screen()
        else:
            if isinstance(locator, str):
                self.get_element(locator).click()
                self.wait_a_moment()
                self.get_screen()
            else:
                locator.click()
                self.wait_a_moment()
                self.get_screen()

    def set_text(self, locator, text, element_name=None):
        if element_name is not None:
            with allure.step(f"Заполнение поля '{element_name}' текстом '{text}'"):
                self.get_element(locator).set_text(text)
        else:
            self.get_element(locator).set_text(text)

    def get_element(self, locator):
        d = self.d
        if locator[0] == '/' and locator[1] == '/':
            return d.xpath(locator)
        else:
            return d(resourceId=locator)

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

    def clear_field(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Удалить текст из поля '{element_name}'"):
                self.get_element(locator).clear_text()
        else:
            self.get_element(locator).clear_text()

    # @allure.step("Получение рандомного элемента")
    def get_random_element(self, locator):
        d = self.d
        if isinstance(locator, str):
            if locator[0] == '/' and locator[1] == '/':
                counter = random.randrange(0, len(d.xpath(locator).all()))
                elements_list = d.xpath(locator).all()
                return elements_list[counter]
            else:
                counter = random.randrange(0, d(resourceId=locator).count)
                return d(resourceId=locator)[counter]
        else:
            counter = random.randrange(0, locator.count)
            return locator[counter]

    def get_random_element_catalog(self, locator):
        d = self.d
        if isinstance(locator, str):
            if locator[0] == '/' and locator[1] == '/':
                counter = random.randrange(3, len(d.xpath(locator).all()) - 2)
                elements_list = d.xpath(locator).all()
                return elements_list[counter]
            else:
                counter = random.randrange(3, d(resourceId=locator).count - 2)
                return d(resourceId=locator)[counter]
        else:
            counter = random.randrange(3, locator.count - 2)
            return locator[counter]

    # @allure.step("Ожидание элемента")
    def wait_element(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Ожидание элемента '{element_name}'"):
                if isinstance(locator, str):
                    if locator[0] == '/' and locator[1] == '/':
                        assert self.get_element(locator).exists == True, print(f"Элемент '{element_name}' отсутствует")
                    else:
                        assert self.get_element(locator).wait(10) == True, print(f"Элемент '{element_name}' отсутствует")
                else:
                    assert locator.wait(10) == True, print(f"Элемент '{element_name}' отсутствует")
        else:
            if isinstance(locator, str):
                if locator[0] == '/' and locator[1] == '/':
                    assert self.get_element(locator).exists == True
                else:
                    assert self.get_element(locator).wait(10) == True
            else:
                assert locator.wait(10) == True

    # @allure.step("Ожидание отсутствия элемента")
    def wait_hidden_element(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Ожидание отсутствия элемента '{element_name}'"):
                if isinstance(locator, str):
                    if locator[0] == '/' and locator[1] == '/':
                        assert self.get_element(locator).exists == False, print(
                            f"Элемент '{element_name}' присутствует на экране")
                    else:
                        assert self.get_element(locator).wait_gone(7) == True, print(
                            f"Элемент '{element_name}' присутствует на экране")
                else:
                    assert locator.wait_gone(7) == True, print(f"Элемент '{element_name}' присутствует на экране")
        else:
            if isinstance(locator, str):
                if locator[0] == '/' and locator[1] == '/':
                    assert self.get_element(locator).exists == False
                else:
                    assert self.get_element(locator).wait_gone(5) == True
            else:
                assert locator.wait_gone(5) == True

    @allure.step("Ожидание на экране текста '{text}'")
    def wait_text(self, text):
        d = self.d
        assert d(textContains=text).wait(10) == True, print(f"Элемент с текстом '{text}' не найден")

    @allure.step("Ожидание отсутствия на экране текста '{text}'")
    def wait_hidden_text(self, text):
        d = self.d
        assert d(textContains=text).wait_gone(10) == True, print(f"Элемент с текстом '{text}' присутствует на экране")

    def close_popup(self):
        self.d.click(0.477, 0.031)

    # @allure.step("Получение числа из элемента (формат int)")
    def get_number_from_element(self, element):
        return int(re.sub('[^0-9]', "", self.get_text(element)))

    @allure.step("Клик по координатам ({x}:{y})")
    def coordinate_click(self, x, y):
        self.d.click(x, y)

    @allure.step("Клик Назад")
    def press_back(self):
        self.d.press("back")

    @allure.step("Проверка заголовка экрана - '{title}'")
    def checking_title_page(self, title):
        d = self.d
        assert d(resourceId='ru.limeshop.android.dev:id/toolbarTitle', text=title).wait(5) == True, print(
            f"Заголовок экрана некорректен. Текущий заголовок - {self.get_text(MainLocators.TOOLBAR_TITLE)}, ожидаемый - {title}")

    @allure.step('Нажать кнопку "X"')
    def click_x(self):
        self.click(MainLocators.X_BUTTON)

    @allure.step('Переход в каталог')
    def open_catalog(self):
        self.wait_element(MainLocators.CATALOG_NAV)
        self.click(MainLocators.CATALOG_NAV, "каталог")

    # @allure.step("Получение количества элементов")
    def get_elements_amount(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            return len(self.get_element(locator).all())
        else:
            return self.get_element(locator).count

    @allure.step('Определяем цвет середины элемента')
    def get_color(self, locator):
        self.wait_element(locator)
        self.get_screen()
        img = Image.open("screen.png")
        center = self.get_element(locator).center()
        pixel_color = img.getpixel(center)
        return pixel_color

    @allure.step('Определяем цвет по координатам')
    def get_color_pixel(self, x, y):
        img = Image.open("screen.png")
        pixel_color = img.getpixel((x, y))
        return pixel_color

    # @allure.step("Элемент с текстом {text}")
    def get_text_element(self, text):
        return self.d.xpath(f'//*[@text="{text}"]')