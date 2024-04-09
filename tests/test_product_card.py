# file: test_product_card.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Карточка товара")
class TestMobile:
    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Кнопка "Купить"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/12")
    def test_size_bottom_sheet(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_cart()
        assert page.get_text(ProductCardLocators.SIZE_INFO) == 'РУКОВОДСТВО ПО РАЗМЕРАМ +'

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Добавление товара в корзину(Плашка)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2943")
    def test_buy_popup(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        assert page.get_text(ProductCardLocators.POPUP_TITLE) == 'Товар добавлен в корзину'
        # ...

    @pytest.mark.smoke
    @allure.title('')
    @allure.testcase("")
    def test_buy_wtf(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.elements_product_card()
        page.card.open_full_product_card()
        page.card.elements_full_product_card()
