import time
import allure
from pages.base_page import BasePage
from locators import *


class CheckOutPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

    @allure.step('Нажать кнопку "Оплатить"')
    def click_pay(self):
        BasePage.swipe_page_up(self)
        time.sleep(0.5)
        self.click(CheckOut.ORDER_PAY)
        time.sleep(2)
        assert self.get_text(SuccessPayScreen.TITLE) == 'ВАШ ЗАКАЗ ПРИНЯТ'
        assert self.get_text(SuccessPayScreen.BUTTON) == 'ПРОДОЛЖИТЬ ПОКУПКИ'
        BasePage.get_screen(self)

    def checkout_set(self, delivery_method, pay_method, date_slot, time_slot):
        with allure.step("Выбрать способ доставки '{delivery_method}'"):
            if delivery_method == '1':
                self.click(CheckOut.DELIVERY_SELECTOR_1)
            elif delivery_method == '2':
                self.click(CheckOut.DELIVERY_SELECTOR_2)
            elif delivery_method == '3':
                self.click(CheckOut.DELIVERY_SELECTOR_3)
            time.sleep(1)
        with allure.step("Выбрать способ оплаты '{pay_method}'"):
            if pay_method == '1':
                self.click(CheckOut.PAYMENT_SELECTOR_1)
            elif pay_method == '2':
                self.click(CheckOut.PAYMENT_SELECTOR_2)
            elif pay_method == '3':
                self.click(CheckOut.PAYMENT_SELECTOR_3)
            elif pay_method == '4':
                self.click(CheckOut.PAYMENT_SELECTOR_4)
            time.sleep(1)
        with allure.step("Выбрать дату доставки '{date_slot}'"):
            if date_slot == '1':
                self.click(CheckOut.SLOTS_DATE_SELECTOR_1)
            elif date_slot == '2':
                self.click(CheckOut.SLOTS_DATE_SELECTOR_2)
            elif date_slot == '3':
                self.click(CheckOut.SLOTS_DATE_SELECTOR_3)
            time.sleep(1)
        with allure.step("Выбрать время доставки '{time_slot}'"):
            if time_slot == '1':
                self.click(CheckOut.SLOTS_TIME_SELECTOR_1)
            elif time_slot == '2':
                self.click(CheckOut.SLOTS_TIME_SELECTOR_2)
            elif time_slot == '3':
                self.click(CheckOut.SLOTS_TIME_SELECTOR_3)
        BasePage.get_screen(self)

    def elements_checkout(self):
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'ОФОРМЛЕНИЕ ЗАКАЗА'
        assert self.get_text(CheckOut.DELIVERY_TITLE) == 'ВЫБЕРИТЕ СПОСОБ ДОСТАВКИ'
        assert self.get_text(CheckOut.PAYMENT_TITLE) == 'ВЫБЕРИТЕ СПОСОБ ОПЛАТЫ'
        assert self.get_text(CheckOut.ORDER_LIST_TITLE) == 'СОСТАВ ЗАКАЗА'

    def elements_checkout_self(self):
        assert self.get_text(CheckOut.PAYMENT_TITLE_4) == 'ПРИ ПОЛУЧЕНИИ'
        assert self.get_text(CheckOut.PAYMENT_INFO_TEXT) == 'Наличными или картой при получении'

    @allure.title('Блок "Оплата" / Успешная оплата (Кнопка продолжить покупки)')
    @allure.testcase("C3050")
    def continue_shopping(self):
        self.click(SuccessPayScreen.BUTTON)
        time.sleep(2)
        assert self.get_text(Catalog.WOMEN) == 'ЖЕНЩИНЫ'
        assert self.get_text(Catalog.MEN) == 'МУЖЧИНЫ'
        assert self.get_text(Catalog.KIDS) == 'ДЕТИ'
        self.is_element_present(MainLocators.X_BUTTON)
        BasePage.get_screen(self)
