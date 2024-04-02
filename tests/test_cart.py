# file: test_cart.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
from pages.cart_page import *
from pages.product_card_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Один товар в корзине')
    @allure.testcase("C29")
    def test_cart_one(self):
        page = MainPage()
        page.open_catalog()
        page.go_to_catalog_item()
        page.go_to_product_card()
        page.cart.add_to_cart()
        page.card.select_size()
        time.sleep(2)
        page.card.open_cart()
        time.sleep(2)
        page.cart.elements_full_cart()
        self.click(CartLocators.CLEAR_ALL)
        page.click(CartLocators.POPUP_CLEAR)

    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Пустой список')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/28")
    def test_clear_cart(self):
        page = MainPage()
        page.clear_basket()
        page.open_cart()
        page.cart.check_empty_cart()

    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Переход в каталог')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/310")
    def test_go_to_card(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        product_name = page.card.get_product_name()
        page.card.open_cart()


