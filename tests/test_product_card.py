# file: test_product_card.py
import pytest
from pages.main_page import MainPage
from pages.product_card_page import ProductCardPage
from pages.base_page import *
import allure


@pytest.fixture(autouse=True)
def clear_app(d):
    MainPage(d).set_nuxt_02()
    MainPage(d).login(valid_email, valid_password)
    MainPage(d).set_feature_toggles()
    time.sleep(2)
    yield
    d.app_clear(package)


class TestMobile:
    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Кнопка "Купить"')
    @allure.testcase("C12")
    def test_size_bottom_sheet(self, d):
        page = ProductCardPage(d)
        MainPage(d).open_product_card_screen()
        page.add_to_cart()
        assert d.xpath(ProductCard.SIZE_INFO).get_text() == 'РУКОВОДСТВО ПО РАЗМЕРАМ +'

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Добавление товара в корзину(Плашка)')
    @allure.testcase("C2943")
    def test_buy_popup(self, d):
        page = ProductCardPage(d)
        MainPage(d).open_product_card_screen()
        page.add_to_cart()
        page.select_size(select_size)
        assert d.xpath(ProductCard.POPUP_TITLE).get_text() == 'Товар добавлен в корзину'
        # Ожидание элементы, чтобы исчезнуть, вернуть True False, Timout по умолчанию для времени ожидания глобальных настроек
        # d.xpath(ProductCard.POPUP).wait_gone(timeout=10)
        # assert d.xpath(ProductCard.POPUP_TITLE).get_text() == 'Товар добавлен в корзину'

    @pytest.mark.smoke
    @allure.title('')
    @allure.testcase("")
    def test_buy_popup(self, d):
        page = ProductCardPage(d)
        MainPage(d).open_product_card_screen()
        page.elements_product_card()
        page.open_full_product_card()
        page.elements_full_product_card()

