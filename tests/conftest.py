import time

import pytest
import uiautomator2 as u2
from config import *
import allure
from pages.main_page import MainPage

d = u2.connect("emulator-5554")


@allure.title("Запустить приложение")
def open_app():
    d.implicitly_wait(10)
    d.app_clear(package)
    d.app_start(package, stop=True)
    page = MainPage()
    page.set_nuxt_02()
    # page.login(valid_email, valid_password)
    # page.set_feature_toggles()


@allure.title("Сменить контур на nuxt02.mp.lmdev")
@pytest.fixture()
def change_nuxt02():
    page = MainPage()
    page.set_nuxt_02()


@allure.title("Авторизоваться")
@pytest.fixture()
def login():
    page = MainPage()
    page.login(valid_email, valid_password)
    page.set_feature_toggles()


@allure.step("Закрытие приложения")
def teardown():
    d.app_stop(package)


@pytest.fixture()
def setup():
    # print('yo')
    open_app()
    yield
    teardown()
