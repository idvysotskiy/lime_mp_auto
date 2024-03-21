# file: test_cart.py
import time
import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from locators import *
import allure


@pytest.mark.usefixtures("setup")
class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Один товар в корзине')
    @allure.testcase("C29")
    def test_cart_one(self):
        page = MainPage()
        page.click_to_nav_catalog()
        page.go_to_catalog_item()
        page.go_to_product_card()
        page.cart.add_to_cart()
        page.card.select_size()
        time.sleep(2)
        page.go_to_cart()
        time.sleep(2)
        page.cart.elements_full_cart()
        self.click(CartLocators.CLEAR_ALL)
        page.click(CartLocators.POPUP_CLEAR)

    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Пустой список')
    @allure.testcase("C28")
    def test_cart_clear(self):
        page = MainPage()
        page.cart.cart_clear()

