import time
import allure
from pages.base_page import BasePage
from locators import *


class CartPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

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
