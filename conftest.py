import os

import pytest
import uiautomator2 as u2
from config import *
import allure

from pages.base_page import BasePage
from pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption('--device', action='store', default='R58N63MW4QR', help='emulator id')


@pytest.fixture
def connect_to_device(request):
    return u2.connect(request.config.getoption('--device'))


# d = u2.connect(device_id)


@allure.title("Запустить приложение")
def open_app(d):
    d.implicitly_wait(10)
    d.app_clear(package)
    d.app_start(package, stop=True)
    # page = MainPage()
    # page.set_contur()
    # page.login(valid_email, valid_password)
    # page.set_feature_toggles()


@allure.title("Сменить контур")
@pytest.fixture()
def change_contur():
    page = MainPage()
    page.set_contur()


@allure.title("Авторизация")
@pytest.fixture()
def login():
    d = u2.connect(os.environ["device_id"])
    page = MainPage(d)
    page.login(valid_email, valid_password)
    # page.set_feature_toggles()


@allure.step("Закрытие приложения")
def teardown(d):
    BasePage(d).get_screen()
    d.app_stop(package)


@pytest.fixture()
def setup(request):
    dev_id = request.config.getoption('--device')
    os.environ["device_id"] = dev_id
    d = u2.connect(dev_id)
    open_app(d)
    page = MainPage(d)
    page.set_contur()
    yield
    teardown(d)
