import time
import allure
from pages.base_page import BasePage
from locators import *
from config import *


class ProductCardPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

    @allure.step('Нажать кнопку "Купить"')
    def add_to_cart(self):
        if self.get_text(ProductCard.BUY) == 'КУПИТЬ':
            self.click(ProductCard.BUY)
        elif self.get_text(ProductCard.BUY_MORE) == 'КУПИТЬ ЕЩЕ':
            self.click(ProductCard.BUY_MORE)

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

    def elements_product_card(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(ProductCard.BUY) == 'КУПИТЬ'
        assert self.get_text(ProductCard.COLORS) == 'Цвета'
        BasePage(self).get_screen()

    def elements_full_product_card(self):
        assert self.get_text(ProductCard.BUY) == 'КУПИТЬ'
        self.is_element_present(ProductCard.FAVORITE)
        self.is_element_present(ProductCard.SHARE)
        self.is_element_present(ProductCard.CART)
        self.is_element_present(ProductCard.ART)
        self.is_element_present(ProductCard.SIZES_GUIDE)
        self.is_element_present(ProductCard.COMPOSITIONS_AND_CARE)
        self.is_element_present(ProductCard.DELIVERY)
        self.is_element_present(ProductCard.PRODUCT_STOCKS)
        self.is_element_present(ProductCard.PAYMENT)
        self.is_element_present(ProductCard.GOES_WELL)
        self.is_element_present(ProductCard.YOU_LIKE_IT)
        BasePage(self).get_screen()

    def open_full_product_card(self):
        self.click(ProductCard.COLORS)
