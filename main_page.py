import time

import allure

from base_page import BasePage
from locators import *
from config import *
from uiautomator2 import UiObject


class MainPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

    @allure.step('Нажать кнопку "X"')
    def click_x(self):
        self.device.xpath(MainLocators.X_BUTTON).click()

    @allure.step('Перейти в каталог')
    def click_to_nav_catalog(self):
        # assert self.device(resourceId=MainLocators.CATALOG_NAV).exist
        self.device.xpath(MainLocators.CATALOG_NAV).click()

    def go_to_catalog_item(self, il1, il2):
        self.device(resourceId=MainLocators.CATALOG_ITEM, text=il1).click()
        self.device(resourceId=MainLocators.CATALOG_ITEM, text=il2).click()

    def add_to_fav_from_catalog(self, product_name):
        self.device(resourceId=MainLocators.FAV_ICON).click()
        name_pr1 = self.device(resourceId=MainLocators.NAME_PRODUCT_COLLECTION, text=product_name).get_text()
        BasePage.cancel_notification(self)
        self.device(resourceId=MainLocators.FAVORITES_NAV).click()
        name_pr2 = self.device(resourceId=MainLocators.NAME_PRODUCT_FAVORITE, text=product_name).get_text()
        assert name_pr1 == name_pr2, 'Наименования товаров не совпадают'

    @allure.step('Авторизоваться')
    def login(self, email, password):
        with allure.step('Открыть Личный кабинет'):
            self.click(MainLocators.PROFILE_NAV)
        with allure.step('Нажать кнопку "Войти"'):
            self.click(Profile.LOGIN_UN)
        with allure.step('Ввести email'):
            self.click(LoginLocators.LOGIN_SCREEN_EMAIL)
            self.device.send_keys(email)
            BasePage.get_screen(self)
        with allure.step('Ввести пароль'):
            self.click(LoginLocators.LOGIN_SCREEN_PASS)
            self.device.send_keys(password)
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
        self.device.xpath(Profile.FEATURE_TOGGLES).click()

    @allure.step('Включить feature toggles')
    def aktivate_feature_toggles(self):
        self.device.xpath(FeatureToggles.SWITCH_1).click()
        self.device.xpath(FeatureToggles.SWITCH_2).click()
        self.device.xpath(FeatureToggles.SWITCH_3).click()
        self.device.xpath(FeatureToggles.SWITCH_4).click()
        BasePage.get_screen(self)

    @allure.step('Заполнить поля валидными данными')
    def enter_valid_registration_data(self, name, surname, phone, password):
        self.device.xpath(LoginLocators.SIGNUP_NAME).click()
        self.device.send_keys(name)
        self.device.xpath(LoginLocators.SIGNUP_SURNAME).click()
        self.device.send_keys(surname)
        self.device.xpath(LoginLocators.SIGNUP_PHONE).click()
        self.device.send_keys(phone)
        self.device.xpath(LoginLocators.SIGNUP_EMAIL).click()
        self.device.send_keys(BasePage.generate_random_email(self))
        # self.device.send_keys('tester23n@lime.com')
        self.device.xpath(LoginLocators.SIGNUP_PASSWORD).click()
        self.device.send_keys(password)
        self.device.xpath(LoginLocators.SIGNUP_REPEAT_PASSWORD).click()
        self.device.send_keys(password)
        BasePage.get_screen(self)

    @allure.step('Выбрать чекбоксы подписок')
    def click_subscribe_boxes(self, subscribes):
        self.device.xpath(LoginLocators.SIGNUP_SUBSCRIBE_WOMEN).click()
        self.device.xpath(LoginLocators.SIGNUP_SUBSCRIBE_MEN).click()
        self.device.xpath(LoginLocators.SIGNUP_SUBSCRIBE_KIDS).click()
        for box in subscribes:
            if box == 'WOMEN':
                self.device.xpath(LoginLocators.SIGNUP_SUBSCRIBE_WOMEN).click()
            if box == 'MEN':
                self.device.xpath(LoginLocators.SIGNUP_SUBSCRIBE_MEN).click()
            if box == 'KIDS':
                self.device.xpath(LoginLocators.SIGNUP_SUBSCRIBE_KIDS).click()
        self.device.xpath(LoginLocators.SIGNUP_SUBSCRIBE_ACCEPT).click()
        BasePage.get_screen(self)

    @allure.step('Нажать кнопку "Продолжить"')
    def click_resume_btn_signup(self):
        self.device.xpath(LoginLocators.SIGNUP_RESUME_BTN).click()

    @allure.step('Отменить уведомления')
    def cancel_notification(self):
        BasePage.cancel_notification(self)

    def screen_title(self, name):
        title_name = self.device(resourceId=MainLocators.TOOLBAR_TITLE).get_text()
        assert name == title_name

    @allure.step('Перейти к карточке товара')
    def go_to_product_card(self):
        self.device.xpath(MainLocators.PRODUCT_CARD_1_1).click()

    @allure.step('Нажать кнопку "Купить"')
    def add_to_cart(self):
        # if self.get_text(ProductCard.BUY) == 'КУПИТЬ':
        self.click(ProductCard.BUY)
        # if self.get_text(ProductCard.BUY_MORE) == "КУПИТ ЕЩЕ":
        #     self.click(ProductCard.BUY_MORE)

    @allure.step('Нажать кнопку "Корзина" в нав.баре')
    def go_to_cart(self):
        self.device.xpath(ProductCard.CART).click()

    @allure.step('Вводим промокод')
    def enter_promo_code(self, promo_code):
        self.device.xpath(Cart.PROMO_CODE).click()
        self.device.send_keys(promo_code)

    @allure.step('Меняем контур на nuxt-02')
    def set_nuxt_02(self):
        self.go_to_profile()
        time.sleep(2)
        self.device.click(0.059, 0.546)

    @allure.step('Включаем feature_toggles')
    def set_feature_toggles(self):
        self.go_to_feature_toggles()
        self.aktivate_feature_toggles()
        self.click_x()
        self.click_x()

    @allure.step('Нажимаем кнопку "К оформлению"')
    def go_to_checkout(self):
        self.device.xpath(Cart.CONTINUE).click()

    @allure.step('Выбрать размер товара')
    def select_size(self, size):
        if size == 'XS':
            self.device.xpath(ProductCard.XS_SIZE).click()
        if size == 'S':
            self.device.xpath(ProductCard.S_SIZE).click()
        if size == 'M':
            self.device.xpath(ProductCard.M_SIZE).click()
        if size == 'L':
            self.device.xpath(ProductCard.L_SIZE).click()
        if size == 'XL':
            self.device.xpath(ProductCard.XS_SIZE).click()


