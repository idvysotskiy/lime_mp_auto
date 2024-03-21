import time
import allure
import pytest
from pages.base_page import BasePage
from locators import *


class CartPage(BasePage):

    @allure.step('Проверить наличие элементов не пустой корзины')
    def elements_full_cart(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'КОРЗИНА'
        assert self.get_text(CartLocators.CLEAR_ALL) == 'ОЧИСТИТЬ'
        self.is_element_present(CartLocators.FAVORITE)
        self.is_element_present(CartLocators.DELETE)
        self.is_element_present(CartLocators.PLUS)
        self.is_element_present(CartLocators.MINUS)
        self.is_element_present(CartLocators.PROMO_CODE)
        assert self.get_text(CartLocators.QUANTITY_TEXT) == 'Количество'
        assert self.get_text(CartLocators.PRICE_TEXT) == 'Стоимость товаров'
        assert self.get_text(CartLocators.SUMMARY_TEXT) == 'ИТОГО'
        assert self.get_text(CartLocators.CONTINUE) == 'К ОФОРМЛЕНИЮ'

    @allure.step('Проверить наличие элементов пустой корзины')
    def elements_clear_cart(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'КОРЗИНА'
        self.is_element_present(CartLocators.ICON)
        self.is_element_present(CartLocators.DESCRIPTION_CLEAR)
        assert self.get_text(CartLocators.BUY_BUTTON) == 'НАЧАТЬ ПОКУПКИ'

    @allure.step('Ввести промокод')
    def enter_promo_code(self, promo_code):
        self.set_text(CartLocators.PROMO_CODE, promo_code)

    @allure.step('Нажать кнопку "К оформлению"')
    def go_to_checkout(self):
        self.click(CartLocators.CONTINUE)

    @allure.step('Очистить корзину')
    def cart_clear(self):
        self.click(CartLocators.CLEAR_ALL)
        self.click(CartLocators.POPUP_CLEAR)


