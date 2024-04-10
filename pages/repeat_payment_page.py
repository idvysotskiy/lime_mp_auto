import time
import allure
from pages.base_page import BasePage
from locators import *


class RepeatPaymentPage(BasePage):

    @allure.step('Нажать кнопку "Повторить попытку"')
    def retry_pay_btn(self):
        self.click(RepeatPayLocators.repeat_pay_btn)
        self.checking_title_page('ИСТОРИЯ ЗАКАЗОВ')

    @allure.step('Оплатить СБП неуспешно')
    def click_pay_sbp_cancel(self):
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)
        self.wait_element(CheckOutLocators.SBP_BANK_LIST_TITLE)
        self.press_back()
        assert self.get_text(MainLocators.POPUP_TITLE) == 'Отменить оплату?'
        # self.wait_text('Отменить оплату?')
        self.click(MainLocators.POPUP_CANCEL)
        assert self.get_text(CheckOutLocators.STATUS_PAY_TITLE) == 'ЗАКАЗ СОЗДАН И ЖДЕТ ОПЛАТЫ'
        # self.wait_text('ЗАКАЗ СОЗДАН И ЖДЕТ ОПЛАТЫ')

    def orders_navigation_check(self):
        self.click_x()
        self.checking_title_page('ЛИЧНЫЙ КАБИНЕТ')
        self.click(ProfileLocators.ORDERS)
        self.checking_title_page('ИСТОРИЯ ЗАКАЗОВ')
