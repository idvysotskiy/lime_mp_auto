# file: test_pay.py
import time
import pytest
from main_page import MainPage
from config import *
from base_page import *
import allure


# @pytest.fixture(autouse=True)
# def clear_app(device):
#     yield
#     device.app_clear(package)


class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("C3048")
    def test_pay_card(self, device):
        page = MainPage(device)
        # Переход на контур nuxt_02
        page.set_nuxt_02()
        time.sleep(2)
        page.login(valid_email, valid_password)
        page.set_feature_toggles()
        page.click_to_nav_catalog()
        page.go_to_catalog_item('РАСПРОДАЖА', 'БРЮКИ')
        page.go_to_product_card()
        page.add_to_cart()
        page.select_size('XS')
        time.sleep(2)
        page.go_to_cart()
        page.enter_promo_code(promo_code_2)
        time.sleep(2)
        page.go_to_checkout()
        page.checkout_set()
        page.click_pay()



