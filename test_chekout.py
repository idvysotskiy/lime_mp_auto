# file: test_favorite.py
import time

import pytest

from main_page import MainPage
from config import *
from base_page import *


# @pytest.fixture(autouse=True)
# def clear_app(device):
#     yield
#     device.app_clear(package)

# @pytest.fixture(autouse=True)
def test_set_nuxt_02(device):
    page = MainPage(device)
    page.go_to_profile()
    time.sleep(5)
    device.click(0.059, 0.546)
    page.login(valid_email, valid_password)
    page.go_to_feature_toggles()
    page.aktivate_feature_toggles()
    page.click_x()
    page.click_x()

# class TestBuy:
#     def test_buy(self, device):







