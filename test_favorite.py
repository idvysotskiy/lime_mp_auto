# file: test_favorite.py
import time

import allure
import pytest

from main_page import MainPage
from config import *
from base_page import *


@pytest.fixture(autouse=True)
def clear_app(device):
    yield
    device.app_clear(package)


class TestMobile:
    @pytest.mark.smoke
    @allure.title('Экран "Основной экран" / Скролл баннеров')
    @allure.testcase("C1861")
    def test_swipe_banner(self, device):
        page = BasePage(device)
        time.sleep(10)
        page.swipe_page_up()
        page.swipe_page_up()
        page.swipe_page_up()
        page.swipe_page_up()
        page.swipe_page_up()
        page.swipe_page_up()

    @pytest.mark.smoke
    @allure.title('Экран "Авторизация" / Авторизация пользователя')
    @allure.testcase("C1016")
    def test_login(self, device):
        page = MainPage(device)
        page.login(valid_email, valid_password)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Добавление в избранное (добавление в список) с экрана "Коллекция"')
    @allure.testcase("C283")
    def test_add_to_fav_from_catalog(self, device):
        page = MainPage(device)
        page.click_to_nav_catalog()
        page.go_to_catalog_item('РАСПРОДАЖА', 'БРЮКИ')
        page.add_to_fav_from_catalog('БРЮКИ ЗАУЖЕННОГО КРОЯ С ЗАЩИПАМИ')

    @pytest.mark.smoke
    @allure.title('Экран "Регистрация" / Заполнение полей "Имя/Фамилия" кириллицей')
    @allure.testcase("C1030")
    def test_reg(self, device):
        page = MainPage(device)
        page.go_to_registration()
        page.enter_valid_registration_data(valid_name_kir, valid_surname_kir, valid_phone, valid_password)
        page.click_subscribe_boxes(subscribe)
        page.click_resume_btn_signup()
        page.cancel_notification()
        page.screen_title('ЛИЧНЫЙ КАБИНЕТ')

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Кнопка "Купить"')
    @allure.testcase("C12")
    def test_size_bottom_sheet(self, device):
        page = MainPage(device)
        page.click_to_nav_catalog()
        page.go_to_catalog_item('РАСПРОДАЖА', 'БРЮКИ')
        page.go_to_product_card()
        page.add_to_cart()
        assert device.xpath(ProductCard.SIZE_INFO).get_text() == 'РУКОВОДСТВО ПО РАЗМЕРАМ +'

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Добавление товара в корзину(Плашка)')
    @allure.testcase("C2943")
    def test_buy_popup(self, device):
        page = MainPage(device)
        page.click_to_nav_catalog()
        page.go_to_catalog_item('РАСПРОДАЖА', 'БРЮКИ')
        page.go_to_product_card()
        page.add_to_cart()
        page.select_size('XS')
        assert device.xpath(ProductCard.POPUP_TITLE).get_text() == 'Товар добавлен в корзину'
        # Ожидание элементы, чтобы исчезнуть, вернуть True False, Timout по умолчанию для времени ожидания глобальных настроек
        # device.xpath(ProductCard.POPUP).wait_gone(timeout=10)
        # assert device.xpath(ProductCard.POPUP_TITLE).get_text() == 'Товар добавлен в корзину'

    # def test_set_nuxt_02(self, device):
    #     page = MainPage(device)
    #     page.go_to_profile()
    #     time.sleep(5)
    #     device.click(0.059, 0.546)
    #     page.login(valid_email, valid_password)
    #     page.go_to_feature_toggles()
    #     page.aktivate_feature_toggles()
    #     page.click_x()
    #     page.click_x()
