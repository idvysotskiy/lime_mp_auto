import time
import allure
import random

import pytest

from pages.base_page import BasePage
from config import *
from locators import *
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckOutPage
from pages.collection_page import CollectionPage
from pages.favorites_page import FavoritesPage
from pages.product_card_page import ProductCardPage
from pages.profile_page import ProfilePage
from pages.repeat_payment_page import RepeatPaymentPage
from pages.search_page import SearchPage


class MainPage(BasePage):
    def __init__(self, d):
        super().__init__(d)
        self.d = d
        self.cart = CartPage(d)
        self.catalog = CatalogPage(d)
        self.checkout = CheckOutPage(d)
        self.card = ProductCardPage(d)
        self.search = SearchPage(d)
        self.favorites = FavoritesPage(d)
        self.profile = ProfilePage(d)
        self.repeat = RepeatPaymentPage(d)
        self.collection = CollectionPage(d)

    @allure.step("Регистрация")
    def user_registration(self):
        self.click(MainLocators.PROFILE_NAV, "иконка профиля")
        self.wait_a_second()
        self.swipe_page_up(2)
        self.wait_a_second()
        self.click(MainLocators.registration_btn, "кнопка Зарегистрироваться")
        self.wait_a_second()
        email = self.generate_random_email()
        self.set_text(MainLocators.name, valid_name_kir, "имя")
        self.set_text(MainLocators.surname, valid_surname_kir, "фамилия")
        self.set_text(MainLocators.phone, valid_phone, "телефон")
        self.set_text(MainLocators.email, email, "почта")
        self.set_text(MainLocators.password, valid_password, "пароль")
        self.set_text(MainLocators.repeat_password, valid_password, "повторение пароля")
        self.swipe_page_up()
        self.wait_a_second()
        self.click(LoginLocators.SIGNUP_SUBSCRIBE_ACCEPT, "чекбокс согласия маркетинговых коммуникаций")
        self.click(MainLocators.continue_btn, "кнопка Продолжить")
        self.wait_a_second()
        self.wait_a_second()
        self.cancel_notification()
        self.wait_a_second()
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'ЛИЧНЫЙ КАБИНЕТ', f'Приложение открыто на экране {self.get_text(MainLocators.TOOLBAR_TITLE)}, а не на экране ЛИЧНЫЙ КАБИНЕТ'
        self.wait_text(email)
        self.click_x()
        return email

    @allure.step('Авторизоваться')
    def login(self, email, password):
        with allure.step('Открыть Личный кабинет'):
            self.click(MainLocators.PROFILE_NAV)
            self.swipe_page_up(2)
            self.wait_a_second()
        with allure.step('Нажать кнопку "Войти"'):
            self.click(ProfileLocators.LOGIN_UN)
        with allure.step('Ввести email'):
            self.set_text(LoginLocators.LOGIN_SCREEN_EMAIL, email)
        with allure.step('Ввести пароль'):
            self.set_text(LoginLocators.LOGIN_SCREEN_PASS, password)
        with allure.step('Нажать кнопку "Войти"'):
            self.click(LoginLocators.LOGIN_SCREEN_SIGNIN)
            self.wait_element(LoginLocators.profile_avatar)
            self.click_x()

    @allure.step('Нажать кнопку "X"')
    def click_x(self):
        self.click(MainLocators.X_BUTTON)

    @allure.step('Переход в каталог')
    def open_catalog(self):
        self.wait_element(MainLocators.CATALOG_NAV)
        self.click(MainLocators.CATALOG_NAV, "каталог")

    @allure.step('Открыть регистрацию')
    def go_to_registration(self):
        self.click(MainLocators.PROFILE_NAV)
        BasePage.swipe_page_up(self)
        self.click(ProfileLocators.SIGNUP_UN)
        BasePage.get_screen(self)

    @allure.step('Переход в личный кабинет')
    def open_profile(self):
        self.click(MainLocators.PROFILE_NAV, "личный кабинет")

    @allure.step('Открыть feature toggles')
    def go_to_feature_toggles(self):
        self.click(ProfileLocators.FEATURE_TOGGLES)

    @allure.step('Включить feature toggles')
    def aktivate_feature_toggles(self):
        self.click(FeatureTogglesLocators.SWITCH_1)
        self.click(FeatureTogglesLocators.SWITCH_2)
        self.click(FeatureTogglesLocators.SWITCH_3)
        self.click(FeatureTogglesLocators.SWITCH_4)
        BasePage.get_screen(self)

    @allure.step('Заполнить поля валидными данными')
    def enter_valid_registration_data(self, name, surname, phone, password):
        self.set_text(LoginLocators.SIGNUP_NAME, name)
        self.set_text(LoginLocators.SIGNUP_SURNAME, surname)
        self.set_text(LoginLocators.SIGNUP_PHONE, phone)
        self.set_text(LoginLocators.SIGNUP_EMAIL, BasePage.generate_random_email(self))
        self.set_text(LoginLocators.SIGNUP_PASSWORD, password)
        self.set_text(LoginLocators.SIGNUP_REPEAT_PASSWORD, password)
        BasePage.get_screen(self)

    @allure.step('Выбрать чекбоксы подписок')
    def click_subscribe_boxes(self, subscribes):
        self.click(LoginLocators.SIGNUP_SUBSCRIBE_WOMEN)
        self.click(LoginLocators.SIGNUP_SUBSCRIBE_MEN)
        self.click(LoginLocators.SIGNUP_SUBSCRIBE_KIDS)
        for box in subscribes:
            if box == 'WOMEN':
                self.click(LoginLocators.SIGNUP_SUBSCRIBE_WOMEN)
            if box == 'MEN':
                self.click(LoginLocators.SIGNUP_SUBSCRIBE_MEN)
            if box == 'KIDS':
                self.click(LoginLocators.SIGNUP_SUBSCRIBE_KIDS)
        self.click(LoginLocators.SIGNUP_SUBSCRIBE_ACCEPT)
        BasePage.get_screen(self)

    @allure.step('Нажать кнопку "Продолжить"')
    def click_resume_btn_signup(self):
        self.click(LoginLocators.SIGNUP_RESUME_BTN)

    # @allure.step('Отменить уведомления')
    # def cancel_notification(self):
    #     BasePage.cancel_notification(self)

    def screen_title(self, name):
        title_name = self.d(resourceId=MainLocators.TOOLBAR_TITLE).get_text()
        assert name == title_name

    # @allure.step('Перейти к карточке товара')
    # def go_to_product_card(self):
    #     try:
    #         self.click(MainLocators.PRODUCT_CARD_1)
    #     except ZeroDivisionError:
    #         try:
    #             self.click(MainLocators.PRODUCT_CARD_1_1)
    #         except Exception:
    #             print('Элемент меню не найден')
    #             raise

    @allure.step("Переход в корзину")
    def open_cart(self):
        self.click(MainLocators.CART_NAV)

    @allure.step('Меняем контур')
    def set_contur(self, contur=QA2):
        self.open_profile()
        self.swipe_page_up()
        time.sleep(2)
        self.click(self.d(textContains=contur).sibling(
            resourceId='ru.limeshop.android.dev:id/item_checkable_option_active'), f"Контур - {contur}")

    @allure.step('Включаем feature_toggles')
    def set_feature_toggles(self):
        self.go_to_feature_toggles()
        self.aktivate_feature_toggles()
        self.click_x()
        self.click_x()

    def reg_kir(self):
        self.go_to_registration()
        self.enter_valid_registration_data(valid_name_kir, valid_surname_kir, valid_phone, valid_password)
        self.click_subscribe_boxes(subscribe)
        self.click_resume_btn_signup()
        self.cancel_notification()

    @allure.step("Очистка корзины")
    def clear_basket(self):
        self.wait_element(MainLocators.CART_NAV)
        if self.d(resourceId='ru.limeshop.android.dev:id/nav_cart').child(
                className='android.widget.TextView').count > 0:
            self.open_cart()
            self.wait_element(CartLocators.CLEAR_ALL)
            self.click(CartLocators.CLEAR_ALL, "кнопка Очистить")
            self.wait_element(CartLocators.POPUP_CLEAR)
            self.click(CartLocators.POPUP_CLEAR, "кнопка Очистить корзину")
            self.wait_text("ВАША КОРЗИНА ПУСТА")
            self.click_x()

    @allure.step("Добавление нового адреса в личном кабинете")
    def add_new_address(self):
        self.click(ProfileLocators.MY_INFO, "мои данные")
        self.click(ProfileLocators.add_new_address_btn, "кнопка Добавить новый адрес")
        self.set_text(ProfileLocators.city, "Новосибирск", "город")
        self.wait_element(ProfileLocators.address_popup)
        self.click(ProfileLocators.address_popup)
        self.set_text(ProfileLocators.street, "Иванова 1", "улица")
        self.wait_element(ProfileLocators.address_popup)
        self.click(ProfileLocators.address_popup)
        self.set_text(ProfileLocators.apartment, "1", "квартира")
        self.click(ProfileLocators.save_address_btn, "кнопка Сохранить")
        self.wait_text("ОБНОВИТЬ ПАРОЛЬ")
        self.click_x()

    @allure.step("Добавление в корзину рандомного товара")
    def add_to_cart_random_product(self):
        self.catalog.open_random_catalog()

        for i in range(3):
            self.catalog.open_random_card()
            self.card.add_to_cart()
            size = self.card.select_random_size()

            if size is True:
                return

        pytest.xfail("Нет доступных размеров в выбранных карточках")

    @allure.step("Ожидание логотипа Lime")
    def wait_logo(self):
        self.wait_element(MainLocators.lime_logo, "логотип Lime")

    def elements_login_screen(self):
        self.wait_element(MainLocators.TOOLBAR_TITLE)
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'ВОЙТИ В АККАУНТ'
        assert self.get_text(LoginLocators.LOGIN_SCREEN_TITLE) == 'ВОЙТИ'
        assert self.get_text(LoginLocators.PASSWORD_RESET_LINK) == 'Забыли данные для входа?'
        assert self.get_text(LoginLocators.LOGIN_BTN) == 'ВОЙТИ'

    @allure.step('Открыть экран "Избранное"')
    def open_favorites(self):
        self.click(MainLocators.FAVORITES_NAV, "кнопка 'Избранное'")
        self.wait_element(FavoritesLocators.TITLE)

    @allure.step('Ввести код из смс')
    def enter_code_from_sms(self, code='0000'):
        self.set_text(LoginLocators.number_text_1, code)

    @allure.step('Авторизоваться по номеру телефона')
    def login_with_phone(self, phone='9639447845'):
        with allure.step('Открыть Личный кабинет'):
            self.click(MainLocators.PROFILE_NAV)
            self.swipe_page_up(2)
            self.wait_a_second()
        with allure.step('Нажать кнопку "Войти"'):
            self.click(ProfileLocators.LOGIN_UN)
            self.set_text(LoginLocators.phone_field, phone)
            self.click(LoginLocators.get_code_button)
            self.enter_code_from_sms()

    @allure.step('Проверяем цвет иконки')
    def icon_color_check(self, locator):
        color = self.get_color(locator)
        assert color == (255, 255, 255), f'Цвет иконки {color} а должен быть (255, 255, 255)'
        self.click(locator)
        color = self.get_color(locator)
        assert color == (0, 0, 0), f'Цвет иконки {color} а должен быть (0, 0, 0)'

    @allure.step('Проверяем цвет иконки Каталог')
    def icon_color_catalog_check(self):
        color = self.get_color(MainLocators.CATALOG_NAV)
        assert color == (255, 255, 255), f'Цвет иконки {color} а должен быть (255, 255, 255)'
        self.open_catalog()
        self.catalog.open_random_catalog()
        color = self.get_color(MainLocators.CATALOG_NAV)
        assert color == (0, 0, 0), f'Цвет иконки {color} а должен быть (0, 0, 0)'

    @allure.step('Переход в поиск')
    def open_search(self):
        self.wait_element(MainLocators.SEARCH_NAV)
        self.click(MainLocators.SEARCH_NAV, "кнопка Поиск")
