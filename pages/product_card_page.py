import time
import allure
from pages.base_page import BasePage
from locators import *
from config import *


class ProductCardPage(BasePage):

    @allure.step('Нажать кнопку "Купить"')
    def add_to_cart(self):
        if self.get_text(ProductCardLocators.BUY) == 'КУПИТЬ':
            self.click(ProductCardLocators.BUY)
        elif self.get_text(ProductCardLocators.BUY_MORE) == 'КУПИТЬ ЕЩЕ':
            self.click(ProductCardLocators.BUY_MORE)

    @allure.step('Выбрать размер товара')
    def select_size(self, size):
        if size == 'XS':
            self.d.xpath(ProductCardLocators.XS_SIZE).click()
        if size == 'S':
            self.d.xpath(ProductCardLocators.S_SIZE).click()
        if size == 'M':
            self.d.xpath(ProductCardLocators.M_SIZE).click()
        if size == 'L':
            self.d.xpath(ProductCardLocators.L_SIZE).click()
        if size == 'XL':
            self.d.xpath(ProductCardLocators.XS_SIZE).click()
        if size == '34':
            self.d.xpath(ProductCardLocators.SIZE_34).click()
        if size == '36':
            self.d.xpath(ProductCardLocators.SIZE_36).click()

    def elements_product_card(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(ProductCardLocators.BUY) == 'КУПИТЬ'
        assert self.get_text(ProductCardLocators.COLORS) == 'Цвета'
        BasePage().get_screen()

    def elements_full_product_card(self):
        assert self.get_text(ProductCardLocators.BUY) == 'КУПИТЬ'
        self.is_element_present(ProductCardLocators.FAVORITE)
        self.is_element_present(ProductCardLocators.SHARE)
        self.is_element_present(ProductCardLocators.CART)
        self.is_element_present(ProductCardLocators.ART)
        self.is_element_present(ProductCardLocators.SIZES_GUIDE)
        self.is_element_present(ProductCardLocators.COMPOSITIONS_AND_CARE)
        self.is_element_present(ProductCardLocators.DELIVERY)
        self.is_element_present(ProductCardLocators.PRODUCT_STOCKS)
        self.is_element_present(ProductCardLocators.PAYMENT)
        self.is_element_present(ProductCardLocators.GOES_WELL)
        self.is_element_present(ProductCardLocators.YOU_LIKE_IT)
        BasePage().get_screen()

    def open_full_product_card(self):
        self.click(ProductCardLocators.COLORS)

    @allure.step("Выбор рандомного размера")
    def select_random_size(self):
        self.get_random_element(ProductCardLocators.product_size_list).click()
        self.wait_a_second()

    def get_product_price(self):
        return self.get_number_from_element(ProductCardLocators.product_price)




