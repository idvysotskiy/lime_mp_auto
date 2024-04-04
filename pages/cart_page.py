import time
import allure
import pytest
from pages.base_page import BasePage
from locators import *


class CartPage(BasePage):

    @allure.step('Проверить наличие элементов не пустой корзины')
    def elements_full_cart(self):
        self.wait_element(MainLocators.X_BUTTON, "кнопка Закрыть")
        self.wait_element(MainLocators.TOOLBAR_TITLE, "заголовок Корзина")
        self.wait_element(CartLocators.CLEAR_ALL, "кнопка Очистить")
        self.wait_element(CartLocators.FAVORITE, "кнопка добавления в избранное")
        self.wait_element(CartLocators.DELETE, "кнопка удаления товара")
        self.wait_element(CartLocators.PLUS, "кнопка увеличения количества")
        self.wait_element(CartLocators.MINUS, "кнопка уменьшения количества")
        self.wait_element(CartLocators.PROMO_CODE, "поле для ввода промокода")
        self.wait_element(CartLocators.QUANTITY_TEXT, "количество")
        self.wait_element(CartLocators.PRICE_TEXT, "цена")
        self.wait_element(CartLocators.SUMMARY_TEXT, "итого")
        self.wait_element(CartLocators.CONTINUE, "кнопка К оформлению")

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

    @allure.step('Клик по кнопке "К оформлению"')
    def go_to_checkout(self):
        self.swipe_page_up()
        self.click(CartLocators.CONTINUE, "кнопка К оформлению")

    @allure.step('Очистка корзины')
    def cart_clear(self):
        self.click(CartLocators.CLEAR_ALL, "кнопка Очистить")
        self.click(CartLocators.POPUP_CLEAR, "кнопка Очистить корзину")

    @allure.step("Проверка пустой корзины")
    def check_empty_cart(self):
        self.wait_text("ВАША КОРЗИНА ПУСТА")
        self.wait_element(CartLocators.BUY_BUTTON, "кнопка Начать покупки")
        self.checking_title_page("КОРЗИНА")
        self.wait_hidden_element(CartLocators.CLEAR_ALL, "кнопка Очистить")

    @allure.step("Переход в карточку товара")
    def open_card(self):
        self.click(CartLocators.card_photo, "фото карточки товара")

    @allure.step("Клик по кнопке Начать покупки")
    def click_start_shopping(self):
        self.click(CartLocators.BUY_BUTTON, "кнопка Начать покупки")
        self.wait_element(CatalogLocators.WOMEN, "заголовок каталога 'Женщины'")

    @allure.step("Проверка наличия в корзине товаров: '{cards_list}'")
    def checking_availability_cards(self, cards_list):
        cards_list_in_cart = []
        elements_list = self.get_element(CartLocators.PRODUCT_TITLE).all()

        for i in range(len(self.get_element(CartLocators.PRODUCT_TITLE).all())):
            cards_list_in_cart.append(elements_list[i].text)

        for i in range(len(cards_list)):
            assert cards_list[i] in cards_list_in_cart, print(f"{cards_list[i]} отсутствует в корзине")

    @allure.step("Увеличение количества товаров")
    def increasing_products_number(self, price_in_card):
        assert int(price_in_card) == self.get_number_from_element(CartLocators.PRICE_TOTAL), print(
            "Сумма товара в карточке и корзине отличаются")
        self.click(CartLocators.PLUS, "кнопка увеличение количества товара")
        self.wait_a_second()
        self.wait_a_second()
        total_price = self.get_number_from_element(CartLocators.PRICE_TOTAL)
        assert int(price_in_card) * 2 == total_price, print(
            "Сумма товара после увеличения не равна сумме товара в карточке * 2")

    @allure.step("Удаление товара из корзины")
    def delete_item(self):
        self.click(CartLocators.DELETE, "кнопка удаления из корзины")
        self.wait_a_second()
        self.wait_a_second()

    @allure.step("Удаление одного товара из корзины и проверка наличия оставшегося товара")
    def remove_one_item(self, cards_list):
        self.delete_item()
        self.wait_hidden_text(cards_list[0])
        self.wait_text(cards_list[1])

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.click(CartLocators.FAVORITE, "кнопка добавления в избранное")


