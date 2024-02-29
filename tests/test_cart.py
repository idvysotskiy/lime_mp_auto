# file: test_cart.py
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
    MainPage(device).click(MainLocators.X_BUTTON)
    yield
    device.app_clear(package)


class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Один товар в корзине')
    @allure.testcase("C29")
    def test_cart_one(self, device):
        page = MainPage(device)
        page.click_to_nav_catalog()
        page.go_to_catalog_item()
        page.go_to_product_card()
        ProductCardPage(device).add_to_cart()
        ProductCardPage(device).select_size(size)
        time.sleep(2)
        page.go_to_cart()
        time.sleep(2)
        page = CartPage(device)
        page.elements_full_cart()
        page.click(Cart.CLEAR_ALL)
        page.click(Cart.POPUP_CLEAR)

    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Пустой список')
    @allure.testcase("C28")
    def test_cart_clear(self, device):
        page = CartPage(device)
        MainPage(device).click(MainLocators.CART_NAV)
        time.sleep(2)
        page.elements_clear_cart()








