# file: test_cart.py
import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
from pages.product_card_page import *
import allure


@pytest.fixture(autouse=True)
def clear_app(d):
    MainPage(d).set_nuxt_02()
    MainPage(d).login(valid_email, valid_password)
    MainPage(d).set_feature_toggles()
    time.sleep(2)
    yield
    d.app_clear(package)


class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Один товар в корзине')
    @allure.testcase("C29")
    def test_cart_one(self, d):
        page = MainPage(d)
        page.click_to_nav_catalog()
        page.go_to_catalog_item()
        page.go_to_product_card()
        ProductCardPage(d).add_to_cart()
        ProductCardPage(d).select_size(select_size)
        time.sleep(2)
        page.go_to_cart()
        time.sleep(2)
        page = CartPage(d)
        page.elements_full_cart()
        page.click(Cart.CLEAR_ALL)
        page.click(Cart.POPUP_CLEAR)

    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Пустой список')
    @allure.testcase("C28")
    def test_cart_clear(self, d):
        page = CartPage(d)
        MainPage(d).click(MainLocators.CART_NAV)
        time.sleep(2)
        page.elements_clear_cart()








