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
        assert self.device.xpath(SuccessPayScreen.TITLE).get_text() == 'ВАШ ЗАКАЗ ПРИНЯТ'
        assert self.device.xpath(SuccessPayScreen.BUTTON).get_text() == 'ПРОДОЛЖИТЬ ПОКУПКИ'
        BasePage.get_screen(self)

    def checkout_set(self, delivery_method, pay_method, date_slot, time_slot):
        with allure.step("Выбрать способ доставки '{delivery_method}'"):
            if delivery_method == '1':
                self.device.xpath(CheckOut.DELIVERY_SELECTOR_1).click()
            elif delivery_method == '2':
                self.device.xpath(CheckOut.DELIVERY_SELECTOR_2).click()
            elif delivery_method == '3':
                self.device.xpath(CheckOut.DELIVERY_SELECTOR_2).click()
            time.sleep(1)
        with allure.step("Выбрать способ оплаты '{pay_method}'"):
            if pay_method == '1':
                self.device.xpath(CheckOut.PAYMENT_SELECTOR_1).click()
            elif pay_method == '2':
                self.device.xpath(CheckOut.PAYMENT_SELECTOR_2).click()
            elif pay_method == '3':
                self.device.xpath(CheckOut.PAYMENT_SELECTOR_3).click()
            elif pay_method == '4':
                self.device.xpath(CheckOut.PAYMENT_SELECTOR_4).click()
            time.sleep(1)
        with allure.step("Выбрать дату доставки '{date_slot}'"):
            if date_slot == '1':
                self.device.xpath(CheckOut.SLOTS_DATE_SELECTOR_1).click()
            elif date_slot == '2':
                self.device.xpath(CheckOut.SLOTS_DATE_SELECTOR_2).click()
            elif date_slot == '3':
                self.device.xpath(CheckOut.SLOTS_DATE_SELECTOR_3).click()
            time.sleep(1)
        with allure.step("Выбрать время доставки '{time_slot}'"):
            if time_slot == '1':
                self.device.xpath(CheckOut.SLOTS_TIME_SELECTOR_1).click()
            elif time_slot == '2':
                self.device.xpath(CheckOut.SLOTS_TIME_SELECTOR_2).click()
            elif time_slot == '3':
                self.device.xpath(CheckOut.SLOTS_TIME_SELECTOR_3).click()
        BasePage.get_screen(self)

    def elements_checkout(self):
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'ОФОРМЛЕНИЕ ЗАКАЗА'
        assert self.get_text(CheckOut.DELIVERY_TITLE) == 'ВЫБЕРИТЕ СПОСОБ ДОСТАВКИ'
        assert self.get_text(CheckOut.PAYMENT_TITLE) == 'ВЫБЕРИТЕ СПОСОБ ОПЛАТЫ'
        assert self.get_text(CheckOut.ORDER_LIST_TITLE) == 'СОСТАВ ЗАКАЗА'

    def elements_checkout_self(self):
        assert self.get_text(CheckOut.PAYMENT_TITLE_4) == 'ПРИ ПОЛУЧЕНИИ'
        assert self.get_text(CheckOut.PAYMENT_INFO_TEXT) == 'Наличными или картой при получении'

    def сontinue_shopping(self):
        self.click(SuccessPayScreen.BUTTON)
        assert self.get_text(Catalog.WOMEN) == 'ЖЕНЩИНЫ'
        assert self.get_text(Catalog.MEN) == 'МУЖЧИНЫ'
        assert self.get_text(Catalog.KIDS) == 'ДЕТИ'


