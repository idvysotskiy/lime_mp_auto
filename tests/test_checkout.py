# file: test_checkout.py
import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
from pages.product_card_page import *
import allure


@pytest.fixture(autouse=True)
def clear_app(device):
    MainPage(device).set_nuxt_02()
    MainPage(device).login(valid_email, valid_password)
    MainPage(device).set_feature_toggles()
    time.sleep(2)
    yield
    device.app_clear(package)


class TestAndroid:
    @allure.title('Экран "Корзина" / Переход к чекауту (Авторизованный)')
    @allure.testcase("C2869")
    def test_checkout_with_one_product(self, device):
        time.sleep(2)
        MainPage(device).click_to_nav_catalog()
        MainPage(device).go_to_catalog_item()
        MainPage(device).go_to_product_card()
        ProductCardPage(device).add_to_cart()
        ProductCardPage(device).select_size(size)
        time.sleep(2)
        MainPage(device).go_to_cart()
        # CartPage(device).enter_promo_code(promo_code_2)
        # time.sleep(2)
        CartPage(device).go_to_checkout()
        time.sleep(4)

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("C3048")
    def test_pay_card(self, device):
        page = CheckOutPage(device)
        self.test_checkout_with_one_product(device)
        page.checkout_set('1', '2', '1', '1')
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("C3038")
    def test_pay_self(self, device):
        page = CheckOutPage(device)
        self.test_checkout_with_one_product(device)
        page.elements_checkout()
        page.checkout_set('1', '4', '2', '2')
        page.elements_checkout_self()
        page.click_pay()
        page.continue_shopping()



