import time
import allure
import pytest

from pages.base_page import BasePage
from locators import *
from pages.main_page import MainPage


class CartPage(BasePage):

    def elements_full_cart(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'КОРЗИНА'
        assert self.get_text(Cart.CLEAR_ALL) == 'ОЧИСТИТЬ'
        self.is_element_present(Cart.FAVORITE)
        self.is_element_present(Cart.DELETE)
        self.is_element_present(Cart.PLUS)
        self.is_element_present(Cart.MINUS)
        self.is_element_present(Cart.PROMO_CODE)
        assert self.get_text(Cart.QUANTITY_TEXT) == 'Количество'
        assert self.get_text(Cart.PRICE_TEXT) == 'Стоимость товаров'
        assert self.get_text(Cart.SUMMARY_TEXT) == 'ИТОГО'
        assert self.get_text(Cart.CONTINUE) == 'К ОФОРМЛЕНИЮ'

    def elements_clear_cart(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'КОРЗИНА'
        self.is_element_present(Cart.ICON)
        self.is_element_present(Cart.DESCRIPTION_CLEAR)
        assert self.get_text(Cart.BUY_BUTTON) == 'НАЧАТЬ ПОКУПКИ'

    @allure.step('Вводим промокод')
    def enter_promo_code(self, promo_code):
        # self.d.xpath(Cart.PROMO_CODE).click()
        # self.d.send_keys(promo_code)
        self.set_text(Cart.PROMO_CODE, promo_code)

    @allure.step('Нажимаем кнопку "К оформлению"')
    def go_to_checkout(self):
        self.click(Cart.CONTINUE)

    @allure.step('Очищяем корзину')
    def cart_clear(self):
        self.click(Cart.CLEAR_ALL)
        self.click(Cart.POPUP_CLEAR)


