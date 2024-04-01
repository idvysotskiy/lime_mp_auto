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
        self.wait_element(ProfileLocators.LOGIN_UN, "кнопка Войти")
        self.wait_element(ProfileLocators.SIGNUP_UN, "кнопка Зарегистрироваться")
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

    @allure.step("Проверка номера в контактах")
    def checking_contacts_phone_number(self):
        phone_number = self.get_number_from_element(ProfileLocators.phone_number)
        self.click(ProfileLocators.phone_number, "номер телефона в контактах")
        self.wait_element(ProfileLocators.dialer_digits, "набранный номер на экране")
        dialer_digits = self.get_text(ProfileLocators.dialer_digits)
        assert str(phone_number) == dialer_digits, print(f"Отображается некорректный номер. В приложении - {phone_number}, в приложении для звонков - {dialer_digits}")


