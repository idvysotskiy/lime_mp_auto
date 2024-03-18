import time
import allure
from pages.base_page import BasePage
from locators import *


class MainPage(BasePage):

    @allure.step('Нажать кнопку "X"')
    def click_x(self):
        self.d.xpath(MainLocators.X_BUTTON).click()

    @allure.step('Перейти в каталог')
    def click_to_nav_catalog(self):
        # assert self.d(resourceId=MainLocators.CATALOG_NAV).exist
        self.click(MainLocators.CATALOG_NAV)

    @allure.step('Перейти в раздел каталога')
    def go_to_catalog_item(self):
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

    @allure.step('Авторизоваться')
    def login(self, email, password):
        with allure.step('Открыть Личный кабинет'):
            self.click(MainLocators.PROFILE_NAV)
        with allure.step('Нажать кнопку "Войти"'):
            self.click(Profile.LOGIN_UN)
        with allure.step('Ввести email'):
            self.click(LoginLocators.LOGIN_SCREEN_EMAIL)
            self.d.send_keys(email)
            BasePage.get_screen(self)
        with allure.step('Ввести пароль'):
            self.click(LoginLocators.LOGIN_SCREEN_PASS)
            self.d.send_keys(password)
            BasePage.get_screen(self)
        with allure.step('Нажать кнопку "Войти"'):
            self.click(LoginLocators.LOGIN_SCREEN_SIGNIN)

    @allure.step('Открыть регистрацию')
    def go_to_registration(self):
        BasePage.swipe_page_up(self)
        self.click(MainLocators.PROFILE_NAV)
        self.click(Profile.SIGNUP_UN)
        BasePage.get_screen(self)

    @allure.step('Открыть личный кабинет')
    def go_to_profile(self):
        self.click(MainLocators.PROFILE_NAV)

    @allure.step('Открыть feature toggles')
    def go_to_feature_toggles(self):
        self.click(Profile.FEATURE_TOGGLES)

    @allure.step('Включить feature toggles')
    def aktivate_feature_toggles(self):
        self.click(FeatureToggles.SWITCH_1)
        self.click(FeatureToggles.SWITCH_2)
        self.click(FeatureToggles.SWITCH_3)
        self.click(FeatureToggles.SWITCH_4)
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
        self.click(ProductCard.CART)

    @allure.step('Меняем контур на nuxt-02')
    def set_nuxt_02(self):
        self.go_to_profile()
        time.sleep(2)
        self.d.click(0.059, 0.546)
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


