import time
import allure
from pages.base_page import BasePage
from locators import *
from config import *


class ProductCardPage(BasePage):

    @allure.step('Клик по кнопке "Купить"')
    def add_to_cart(self):
        self.click(ProductCardLocators.BUY, "кнопка Купить")
        self.wait_a_moment()

    def elements_product_card(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(ProductCardLocators.BUY) == 'КУПИТЬ'
        assert self.get_text(ProductCardLocators.COLORS) == 'Цвета'
        self.get_screen()

    @allure.step("Проверка наличия элементов карточки товара")
    def checking_card_elements(self):
        self.wait_element(ProductCardLocators.BUY, "Купить")
        self.wait_element(ProductCardLocators.FAVORITE, "Избранное")
        self.wait_element(ProductCardLocators.SHARE, "Поделиться")
        self.wait_element(ProductCardLocators.CART, "Корзина")
        self.d.swipe(self.get_element(ProductCardLocators.product_name).center()[0], self.get_element(ProductCardLocators.product_name).center()[1], self.get_element(ProductCardLocators.product_name).center()[0], self.get_element(ProductCardLocators.product_name).center()[1] + 500)
        self.wait_element(ProductCardLocators.ART, "Артикул")
        self.wait_element(ProductCardLocators.SIZES_GUIDE, "Руководство по размерам")
        self.wait_element(ProductCardLocators.COMPOSITIONS_AND_CARE, "Состав и уход")
        self.wait_element(ProductCardLocators.DELIVERY, "Доставка и возврат")
        self.wait_element(ProductCardLocators.PRODUCT_STOCKS, "Наличие в магазинах")
        self.swipe_page_up()
        self.wait_element(ProductCardLocators.PAYMENT, "Оплата")
        # self.wait_element(ProductCardLocators.GOES_WELL)
        # self.wait_element(ProductCardLocators.YOU_LIKE_IT)
        self.get_screen()

    def open_full_product_card(self):
        self.click(ProductCardLocators.COLORS)

    @allure.step("Свайп к описанию")
    def swipe_in_card(self):
        product_name_bound = self.get_element(ProductCardLocators.product_name).center()
        self.d.swipe(product_name_bound[0], product_name_bound[1], product_name_bound[0], product_name_bound[1] - 700)

    @allure.step("Выбор рандомного размера")
    def select_random_size(self):
        if len(self.get_element(ProductCardLocators.available_size).all()) > 0:
            self.get_random_element(ProductCardLocators.available_size).click()
            self.wait_a_second()
            return True
        else:
            self.press_back()
            self.press_back()

    # @allure.step("Получение цены товара")
    def get_product_price(self):
        return self.get_number_from_element(ProductCardLocators.product_price)

    @allure.step('Переход в корзину')
    def open_cart(self):
        self.click(ProductCardLocators.CART, "кнопка корзины")

    # @allure.step("Получение названия товара")
    def get_product_name(self):
        return self.get_text(ProductCardLocators.product_name)

    @allure.step('Добавление/удаление из избранного')
    def add_to_favorites(self):
        self.click(ProductCardLocators.FAVORITE, 'Кнопка добавления/удаления из избранного')
        product_name = self.get_product_name()
        return product_name

    @allure.step("Добавление в корзину второго размера одного товара")
    def add_to_cart_more_item(self, size):
        self.click(ProductCardLocators.BUY_MORE, "кнопка Купить еще")
        self.click(self.get_random_element(
            f'//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]//android.widget.TextView['
            f'@resource-id="ru.limeshop.android.dev:id/product_add_to_cart_name" and not('
            f'following-sibling::android.widget.TextView['
            f'@resource-id="ru.limeshop.android.dev:id/product_add_to_cart_available"]) and not(@text="{size}")]'),
            "рандомный размер")

    @allure.step("Клик по кнопке Назад")
    def click_back(self):
        self.click(ProductCardLocators.back_btn, "кнопка Назад")

    @allure.step("Клик по кнопке Поделиться")
    def click_share(self):
        self.click(ProductCardLocators.SHARE, "кнопка Поделиться")

    @allure.step("Клик по кнопке Доставка и возврат")
    def click_delivery(self):
        self.click(ProductCardLocators.DELIVERY, "кнопка Доставка и возврат")
        self.wait_element(ProductCardLocators.delivery_description_page, "описание доставки и возврата")
        self.wait_text("ДОСТАВКА И ВОЗВРАТ")
        self.wait_text("СРОКИ ДОСТАВКИ")
