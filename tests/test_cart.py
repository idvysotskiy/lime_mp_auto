# file: test_cart.py
import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
import allure


# @pytest.fixture(autouse=True)
# def clear_app(device):
#     yield
#     device.app_clear(package)


class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Один товар в корзине')
    @allure.testcase("C29")
    def test_cart_one(self, device):
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
        time.sleep(2)
        page = CartPage(device)
        page.elements_full_cart()
        page.click(Cart.CLEAR_ALL)

    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Пустой список')
    @allure.testcase("C28")
    def test_cart_clear(self, device):
        page = CartPage(device)
        MainPage(device).click(MainLocators.CART_NAV)
        time.sleep(2)
        page.elements_clear_cart()







