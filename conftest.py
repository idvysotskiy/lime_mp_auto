import pytest
import uiautomator2 as u2
from config import *
import allure

from pages.base_page import BasePage
from pages.main_page import MainPage

d = u2.connect(device_id)


@allure.title("Запустить приложение")
def open_app():
    d.implicitly_wait(10)
    d.app_clear(package)
    d.app_start(package, stop=True)
    # page = MainPage()
    # page.set_nuxt_02()
    # page.login(valid_email, valid_password)
    # page.set_feature_toggles()


@allure.title("Сменить контур на nuxt02.mp.lmdev")
@pytest.fixture()
def change_nuxt02():
    page = MainPage()
    page.set_nuxt_02()


@allure.title("Авторизация")
@pytest.fixture()
def login():
    page = MainPage()
    page.login(valid_email, valid_password)
    # page.set_feature_toggles()


@allure.step("Закрытие приложения")
def teardown():
    BasePage().get_screen()
    d.app_stop(package)
    d.service('uiautomator').stop()


@pytest.fixture()
def setup():
    d.service('uiautomator').start()
    open_app()
    yield
    teardown()
