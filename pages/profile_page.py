import time
import allure
from pages.base_page import BasePage
from locators import *
from config import *


class ProfilePage(BasePage):
    @allure.step("Проверка наличия элементов личного кабинета")
    def checking_account_elements(self):
        self.checking_title_page("ЛИЧНЫЙ КАБИНЕТ")
        self.wait_element(ProfileLocators.MANUAL_UN, "Руководство по покупке")
        self.wait_element(ProfileLocators.CONTACTS_UN, "Контакты")
        self.wait_element(ProfileLocators.COMPANY_UN, "Компания")
        self.wait_element(ProfileLocators.SHOPS_UN, "Магазины")
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_UN, "Подписки и уведомления")
        self.swipe_page_up(2)
        self.wait_element(ProfileLocators.CHAT_UN, "Чат")
        self.wait_element(ProfileLocators.LOGIN_AND_SIGN, "Кнопка Войти или Зарегистрироваться")
        self.wait_text("ОЦЕНИТЕ ПРИЛОЖЕНИЕ")
        self.wait_text("Политика конфиденциальности")
        self.wait_text("Условия покупки")
        self.wait_text("ВЕРСИЯ")
        self.wait_element(ProfileLocators.app_id, "id приложения")

    @allure.step("Закрытие личного кабинета")
    def close_account(self):
        self.click(MainLocators.X_BUTTON, "кнопка Закрытия экрана")

    @allure.step("Переход в раздел Руководство по покупке")
    def open_manual(self):
        self.click(ProfileLocators.MANUAL_UN, "руководство по покупке")
        self.wait_text("lime-shop.com/ru_ru/help")

    @allure.step("Переход в раздел Контакты")
    def open_contacts(self):
        self.click(ProfileLocators.CONTACTS_UN, "контакты")
        self.checking_title_page("КОНТАКТЫ")

    @allure.step("Переход в раздел Компания")
    def open_company(self):
        self.click(ProfileLocators.COMPANY_UN, "компания")
        self.checking_title_page("О КОМПАНИИ")

    @allure.step("Переход в раздел Магазины")
    def open_shops(self):
        self.click(ProfileLocators.SHOPS_UN, "Магазины")
        # self.checking_title_page("Магазины")

    @allure.step("Проверка номера в контактах")
    def checking_contacts_phone_number(self):
        phone_number = self.get_number_from_element(ProfileLocators.phone_number)
        self.click(ProfileLocators.phone_number, "номер телефона в контактах")
        self.wait_element(ProfileLocators.dialer_digits, "набранный номер на экране")
        dialer_digits = self.get_text(ProfileLocators.dialer_digits)
        assert str(phone_number) == dialer_digits, print(
            f"Отображается некорректный номер. В приложении - {phone_number}, в приложении для звонков - {dialer_digits}")

    @allure.step("Логаут")
    def logout(self):
        self.click(MainLocators.PROFILE_NAV)
        self.swipe_page_up(3)
        self.wait_a_second()
        self.click(ProfileLocators.LOGOUT, "кнопка Выйти")
        self.wait_element(ProfileLocators.LOGIN_UN, "кнопка Войти")

    @allure.step('Проверка отсутсвия элементов')
    def exit_from_profile(self):
        self.click_x()
        self.wait_hidden_element(ProfileLocators.MANUAL_UN, "Руководство по покупке")
        self.wait_hidden_element(ProfileLocators.CONTACTS_UN, "Контакты")
        self.wait_hidden_element(ProfileLocators.COMPANY_UN, "Компания")
        self.wait_hidden_element(ProfileLocators.SHOPS_UN, "Магазины")
        self.wait_hidden_element(ProfileLocators.SUBSCRIPTIONS_UN, "Подписки и уведомления")

    @allure.step("Проверка номера в контактах")
    def checking_shops_elements(self):
        if self.get_element(ProfileLocators.PERMISSION_SCREEN):
            self.click(ProfileLocators.ONE_USE)
        self.wait_element(ProfileLocators.SHOP_MAP)
        self.wait_element(ProfileLocators.SHOP_LIST)
        self.wait_element(ProfileLocators.SHOPS_VIEW_LIST)
        self.wait_element(ProfileLocators.SHOPS_PARTS_FILTERS)

    @allure.step('Открытие экрана "Подписки и Уведомления')
    def open_subscribed_screen(self):
        self.click(ProfileLocators.SUBSCRIPTIONS_UN)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_TITLE)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_WOMEN)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_WOMEN_CHBX)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_MEN)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_MEN_CHBX)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_KIDS)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_KIDS_CHBX)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_MAIL)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_MAIL_SWITCH)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_PUSH)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_PUSH_SWITCH)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_BTN_SAVE)
        self.wait_element(ProfileLocators.SUBSCRIPTIONS_BTN_BACK)


