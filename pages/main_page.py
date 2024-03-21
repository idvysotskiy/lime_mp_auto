import time
import allure
import random
from pages.base_page import BasePage
from locators import *
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckOutPage
from pages.favorites_page import FavoritesPage
from pages.product_card_page import ProductCardPage
from pages.search_page import SearchPage


class MainPage(BasePage):
    cart = CartPage()
    catalog = CatalogPage()
    checkout = CheckOutPage()
    card = ProductCardPage()
    search = SearchPage()
    favorites = FavoritesPage()

    @allure.step("Регистрация")
    def user_registration(self):
        self.click(MainLocators.PROFILE_NAV, "иконка профиля")
        self.swipe_page_up()
        self.click(MainLocators.registration_btn, "кнопка Зарегистрироваться")
        self.wait_a_second()
        email = 'test' + str(random.randint(0, 999999999)) + '@test.ru'
        self.set_text(MainLocators.name, 'Test', "имя")
        self.set_text(MainLocators.surname, 'Testov', "фамилия")
        self.set_text(MainLocators.phone, '9998887755', "телефон")
        self.set_text(MainLocators.email, email, "почта")
        self.set_text(MainLocators.password, '87654321', "пароль")
        self.set_text(MainLocators.repeat_password, '87654321', "повторение пароля")
        self.swipe_page_up()
        self.click(MainLocators.approve_checkbox, 'чекбокс Я даю согласие на получение маркетинговых коммуникаций')
        self.click(MainLocators.continue_btn, "кнопка Продолжить")
        self.wait_text(email)
        self.click_x()
        return email

    @allure.step('Авторизоваться')
    def login(self, email, password):
        with allure.step('Открыть Личный кабинет'):
            self.click(MainLocators.PROFILE_NAV)
            self.swipe_page_up()
            self.swipe_page_up()
        with allure.step('Нажать кнопку "Войти"'):
            self.click(ProfileLocators.LOGIN_UN)
        with allure.step('Ввести email'):
            # self.click(LoginLocators.LOGIN_SCREEN_EMAIL)
            self.set_text('//*[@resource-id="ru.limeshop.android.dev:id/signin_email"]', email)
            # BasePage.get_screen(self)
        with allure.step('Ввести пароль'):
            # self.click(LoginLocators.LOGIN_SCREEN_PASS)
            self.set_text('//*[@resource-id="ru.limeshop.android.dev:id/signin_password"]', password)
            # self.d.xpath('//*[@resource-id="ru.limeshop.android.dev:id/signin_password"]/android.view.ViewGroup[1]/android.widget.EditText[1]').send_keys(password)
            # BasePage.get_screen(self)
        with allure.step('Нажать кнопку "Войти"'):
            self.click(LoginLocators.LOGIN_SCREEN_SIGNIN)
            self.wait_element(LoginLocators.profile_avatar)
            self.click_x()

    @allure.step('Нажать кнопку "X"')
    def click_x(self):
        self.click(MainLocators.X_BUTTON)

    @allure.step('Переход в каталог')
    def click_to_nav_catalog(self):
        self.wait_element(MainLocators.CATALOG_NAV)
        self.click(MainLocators.CATALOG_NAV, "каталог")

    @allure.step('Перейти в раздел каталога')
    def go_to_catalog_item(self):
        # self.click(self.get_random_element(Catalog.MENU_ITEM))
        try:
            self.click(MainLocators.MENU_ITEM_1)
        except ZeroDivisionError:
            pass
        try:
            self.click(MainLocators.MENU_ITEM_2)
        except Exception:
            print('Элемент меню не найден')
            raise

    @allure.step('Добавить товар в избранное')
    def add_to_fav_from_catalog(self):
        self.click(MainLocators.FAV_ICON)
        product_name_1 = self.d(resourceId=MainLocators.NAME_PRODUCT_COLLECTION, text=product_name).get_text()
        BasePage.cancel_notification(self)
        # product_name_1 = self.get_text(MainLocators.ITEM)
        self.click(MainLocators.FAVORITES_NAV)
        time.sleep(1)
        product_name_2 = self.d(resourceId=MainLocators.NAME_PRODUCT_FAVORITE, text=product_name).get_text()
        assert product_name_1 == product_name_2, 'Наименования товаров не совпадают'

    @allure.step('Открыть регистрацию')
    def go_to_registration(self):
        self.click(MainLocators.PROFILE_NAV)
        BasePage.swipe_page_up(self)
        self.click(ProfileLocators.SIGNUP_UN)
        BasePage.get_screen(self)

    @allure.step('Открыть личный кабинет')
    def go_to_profile(self):
        self.click(MainLocators.PROFILE_NAV)

    @allure.step('Открыть feature toggles')
    def go_to_feature_toggles(self):
        self.click(ProfileLocators.FEATURE_TOGGLES)

    # @allure.step('Включить feature toggles')
    # def aktivate_feature_toggles(self):
    #     self.click(FeatureTogglesLocators.SWITCH_1)
    #     self.click(FeatureTogglesLocators.SWITCH_2)
    #     self.click(FeatureTogglesLocators.SWITCH_3)
    #     self.click(FeatureTogglesLocators.SWITCH_4)
    #     BasePage.get_screen(self)

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

    @allure.step('Отменить уведомления')
    def cancel_notification(self):
        BasePage.cancel_notification(self)

    def screen_title(self, name):
        title_name = self.d(resourceId=MainLocators.TOOLBAR_TITLE).get_text()
        assert name == title_name

    @allure.step('Перейти к карточке товара')
    def go_to_product_card(self):
        try:
            self.click(MainLocators.PRODUCT_CARD_1)
        except ZeroDivisionError:
            try:
                self.click(MainLocators.PRODUCT_CARD_1_1)
            except Exception:
                print('Элемент меню не найден')
                raise

    @allure.step('Нажать кнопку "Корзина" в нав.баре')
    def go_to_cart(self):
        self.click(ProductCardLocators.CART)

    @allure.step('Меняем контур на nuxt-02')
    def set_nuxt_02(self):
        self.go_to_profile()
        time.sleep(2)
        self.d.click(0.062, 0.508)
        time.sleep(2)

    @allure.step('Включаем feature_toggles')
    def set_feature_toggles(self):
        self.go_to_feature_toggles()
        self.aktivate_feature_toggles()
        self.click_x()
        self.click_x()

    def open_product_card_screen(self):
        self.click_to_nav_catalog()
        self.go_to_catalog_item(menu_l1, menu_l2)
        self.go_to_product_card()

    def reg_kir(self):
        self.go_to_registration()
        self.enter_valid_registration_data(valid_name_kir, valid_surname_kir, valid_phone, valid_password)
        self.click_subscribe_boxes(subscribe)
        self.click_resume_btn_signup()
        self.cancel_notification()
