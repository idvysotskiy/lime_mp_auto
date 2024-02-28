# file: test_pay.py
import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
from pages.product_card_page import *
import allure


# @pytest.fixture(autouse=True)
# def clear_app(device):
#     MainPage(device).set_nuxt_02()
#     MainPage(device).login(valid_email, valid_password)
#     page.set_feature_toggles()
#     time.sleep(2)
#     MainPage(device).click(MainLocators.X_BUTTON)
#     yield
#     device.app_clear(package)


class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("C3048")
    def test_pay_card(self, device):
        page = CartPage(device)
        MainPage(device).click_to_nav_catalog()
        MainPage(device).go_to_catalog_item()
        MainPage(device).go_to_product_card()
        ProductCardPage(device).add_to_cart()
        ProductCardPage(device).select_size(size)
        time.sleep(2)
        MainPage(device).go_to_cart()
        page.enter_promo_code(promo_code_2)
        time.sleep(2)
        page.go_to_checkout()
        page = CheckOutPage(device)
        page.checkout_set('1', '2', '1', '1')
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("C3038")
    def test_pay_self(self, device):
        page = MainPage(device)
        # Переход на контур nuxt_02
        page.set_nuxt_02()
        time.sleep(2)
        page.login(valid_email, valid_password)
        page.set_feature_toggles()
        page.click_to_nav_catalog()
        page.go_to_catalog_item('РАСПРОДАЖА', 'ВСЕ МОДЕЛИ')
        page.go_to_product_card()
        time.sleep(2)
        page.add_to_cart()
        page.select_size('XS')
        time.sleep(2)
        page.go_to_cart()
        time.sleep(2)
        page.go_to_checkout()
        page = CheckOutPage(device)
        page.elements_checkout()
        page.checkout_set('1', '4', '2', '2')
        page.elements_checkout_self()
        page.click_pay()
        page.continue_shopping()



