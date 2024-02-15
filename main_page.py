from base_page import BasePage
from locators import *
from config import *
from uiautomator2 import UiObject


class MainPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

    def click_x(self):
        self.device.xpath(MainLocators.X_BUTTON).click()

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

    def login(self, email, password):
        self.device(resourceId=MainLocators.PROFILE_NAV).click()
        self.device(resourceId=Profile.LOGIN_UN).click()
        self.device(resourceId=LoginLocators.LOGIN_SCREEN_EMAIL).click()
        self.device.send_keys(email)
        self.device(resourceId=LoginLocators.LOGIN_SCREEN_PASS).click()
        self.device.send_keys(password)
        self.device(resourceId=LoginLocators.LOGIN_SCREEN_SIGNIN).click()

    def go_to_registration(self):
        self.device(resourceId=MainLocators.PROFILE_NAV).click()
        self.device(resourceId=Profile.SIGNUP_UN).click()

    def go_to_profile(self):
        self.device(resourceId=MainLocators.PROFILE_NAV).click()

    def go_to_feature_toggles(self):
        self.device.xpath(Profile.FEATURE_TOGGLES).click()

    def aktivate_feature_toggles(self):
        self.device.xpath(FeatureToggles.SWITCH_1).click()
        self.device.xpath(FeatureToggles.SWITCH_2).click()
        self.device.xpath(FeatureToggles.SWITCH_3).click()

    def enter_valid_registration_data(self, name, surname, phone, password):
        self.device.xpath(LoginLocators.SIGNUP_NAME).click()
        self.device.send_keys(name)
        self.device.xpath(LoginLocators.SIGNUP_SURNAME).click()
        self.device.send_keys(surname)
        self.device.xpath(LoginLocators.SIGNUP_PHONE).click()
        self.device.send_keys(phone)
        self.device.xpath(LoginLocators.SIGNUP_EMAIL).click()
        self.device.send_keys(BasePage.generate_random_email(self))
        self.device.xpath(LoginLocators.SIGNUP_PASSWORD).click()
        self.device.send_keys(password)
        self.device.xpath(LoginLocators.SIGNUP_REPEAT_PASSWORD).click()
        self.device.send_keys(password)

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

    def click_resume_btn_signup(self):
        self.device.xpath(LoginLocators.SIGNUP_RESUME_BTN).click()

    def cancel_notification(self):
        BasePage.cancel_notification(self)

    def screen_title(self, name):
        title_name = self.device(resourceId=MainLocators.TOOLBAR_TITLE).get_text()
        assert name == title_name

    def go_to_product_card(self):
        self.device.xpath(MainLocators.PRODUCT_CARD_1_1).click()

    def add_to_cart(self):
        self.device.xpath(ProductCard.BUY).click()

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

    def set_contur_nuxt_02(self):
        self.device.click(0.065, 0.68)

    def cat_men(self):
        self.device.xpath(MainLocators.)

