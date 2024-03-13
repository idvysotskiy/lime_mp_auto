import pytest
import uiautomator2 as u2
from config import *
import allure


@allure.title("Запустить приложение")
@pytest.fixture
def d():
    device_id = 'emulator-5554'
    device = u2.connect(device_id)
    device.app_clear(package)
    device.app_start(package, stop=True)
    # device.xpath.global_set("timeout", 10)
    # device.implicitly_wait(10.0)
    return device



