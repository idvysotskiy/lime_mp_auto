# file: test_product_card.py
import pytest
from pages.main_page import MainPage
from pages.product_card_page import ProductCardPage
from pages.base_page import *
import allure


@pytest.fixture(autouse=True)
def clear_app(device):
    MainPage(device).set_nuxt_02()
    MainPage(device).login(valid_email, valid_password)
    MainPage(device).set_feature_toggles()
    time.sleep(2)
    yield
    device.app_clear(package)


class TestMobile:
    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Кнопка "Купить"')
    @allure.testcase("C12")
    def test_size_bottom_sheet(self, device):
        page = ProductCardPage(device)
        MainPage(device).click_to_nav_catalog()
        MainPage(device).go_to_catalog_item(menu_l1, menu_l2)
        MainPage(device).go_to_product_card()
        page.add_to_cart()
        assert device.xpath(ProductCard.SIZE_INFO).get_text() == 'РУКОВОДСТВО ПО РАЗМЕРАМ +'

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Добавление товара в корзину(Плашка)')
    @allure.testcase("C2943")
    def test_buy_popup(self, device):
        page = ProductCardPage(device)
        MainPage(device).click_to_nav_catalog()
        MainPage(device).go_to_catalog_item(menu_l1, menu_l2)
        MainPage(device).go_to_product_card()
        page.add_to_cart()
        page.select_size(select_size)
        assert device.xpath(ProductCard.POPUP_TITLE).get_text() == 'Товар добавлен в корзину'
        # Ожидание элементы, чтобы исчезнуть, вернуть True False, Timout по умолчанию для времени ожидания глобальных настроек
        # device.xpath(ProductCard.POPUP).wait_gone(timeout=10)
        # assert device.xpath(ProductCard.POPUP_TITLE).get_text() == 'Товар добавлен в корзину'
