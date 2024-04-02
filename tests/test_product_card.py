# file: test_product_card.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestMobile:
    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Кнопка "Купить"')
    @allure.testcase("C12")
    def test_size_bottom_sheet(self):
        page = MainPage()
        page.open_product_card_screen()
        page.cart.add_to_cart()
        assert page.get_text(ProductCardLocators.SIZE_INFO) == 'РУКОВОДСТВО ПО РАЗМЕРАМ +'

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Добавление товара в корзину(Плашка)')
    @allure.testcase("C2943")
    def test_buy_popup(self):
        page = MainPage()
        page.open_product_card_screen()
        page.cart.add_to_cart()
        page.cart.select_size(select_size)
        assert page.get_text(ProductCardLocators.POPUP_TITLE) == 'Товар добавлен в корзину'
        # ...

    @pytest.mark.smoke
    @allure.title('')
    @allure.testcase("")
    def test_buy_popup(self):
        page = MainPage()
        page.open_product_card_screen()
        page.card.elements_product_card()
        page.card.open_full_product_card()
        page.card.elements_full_product_card()
