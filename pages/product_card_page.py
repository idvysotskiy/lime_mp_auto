import time
import allure
from pages.base_page import BasePage
from locators import *


class ProductCardPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

    @allure.step('Нажать кнопку "Купить"')
    def add_to_cart(self):
        # if self.get_text(ProductCard.BUY) == 'КУПИТЬ':
        self.click(ProductCard.BUY)
        # if self.get_text(ProductCard.BUY_MORE) == "КУПИТ ЕЩЕ":
        #     self.click(ProductCard.BUY_MORE)

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