import time
import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from locators import *
from config import *


class ProductCardPage(BasePage):

    @allure.step('Нажать кнопку "Купить"')
    def add_to_cart(self):
        if self.get_text(ProductCard.BUY) == 'КУПИТЬ':
            self.click(ProductCard.BUY)
        elif self.get_text(ProductCard.BUY_MORE) == 'КУПИТЬ ЕЩЕ':
            self.click(ProductCard.BUY_MORE)

    @allure.step('Выбрать размер товара')
    def select_size(self, size):
        if size == 'XS':
            self.d.xpath(ProductCard.XS_SIZE).click()
        if size == 'S':
            self.d.xpath(ProductCard.S_SIZE).click()
        if size == 'M':
            self.d.xpath(ProductCard.M_SIZE).click()
        if size == 'L':
            self.d.xpath(ProductCard.L_SIZE).click()
        if size == 'XL':
            self.d.xpath(ProductCard.XS_SIZE).click()
        if size == '34':
            self.d.xpath(ProductCard.SIZE_34).click()
        if size == '36':
            self.d.xpath(ProductCard.SIZE_36).click()

    def elements_product_card(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(ProductCard.BUY) == 'КУПИТЬ'
        assert self.get_text(ProductCard.COLORS) == 'Цвета'
        BasePage().get_screen()

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
        BasePage().get_screen()

    def open_full_product_card(self):
        self.click(ProductCard.COLORS)

    def add_one_product_to_cart(self):
        main = MainPage()
        main.click_to_nav_catalog()
        main.go_to_catalog_item()
        main.go_to_product_card()
        self.add_to_cart()
        self.select_size(select_size)
        time.sleep(2)
        main.go_to_cart()


