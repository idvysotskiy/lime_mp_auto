import random
import re

import allure
from locators import MainLocators, ProductCardLocators, CatalogLocators, CollectionLocators
from pages.base_page import BasePage


class CollectionPage(BasePage):

    @allure.step("Получение названия товара")
    def get_product_name(self):
        return self.get_text(CollectionLocators.CARDNAME)

    @allure.step('Добавить в избранное с экрана "Коллекция"')
    def add_to_favorite(self, name=None):
        if name is None:
            self.click(CollectionLocators.FAVORITEBUTTON)
            product_name = self.get_product_name()
            return product_name
        else:
            self.click(CollectionLocators.FAVORITEBUTTON)

    @allure.step('Проверка наличия товара в Избранном, добавленное из коллекции')
    def checking_availability_cards(self, cards_list):
        cards_list_in_favorite = []
        elements_list = self.get_element(CollectionLocators.CARDNAME).all()

        for i in range(len(self.get_element(CollectionLocators.CARDNAME).all())):
            cards_list_in_favorite.append(elements_list[i].text)

        for i in range(len(cards_list)):
            assert cards_list[i] in cards_list_in_favorite, print(f"{cards_list[i]} отсутствует в избранном")

    # @allure.step("Сортировать по возрастанию цены")
    # def sort_upper_price(self):
    #     self.click(CollectionLocators.filter_price_asc_cbox)
    #     self.click(CollectionLocators.filter_apply_btn)
    #     self.wait_element(CollectionLocators.SCREENFORCARDS)
    #     bounds = self.get_element(CollectionLocators.SCREENFORCARDS).bounds()
    #     cards = self.get_element(CollectionLocators.CARDPLACE).all()
    #     evenbounds = cards[1].bounds
    #     assert evenbounds[2] >= bounds[2] / 2
    #     oddbounds = cards[2].bounds
    #     assert oddbounds[2] <= bounds[2] / 2
    #     price_cards = self.get_element(CollectionLocators.PRICELIST).all()
    #     price_cards_text = []
    #     for i in range(len(price_cards)):
    #        # price_cards_text.append(int(re.sub('[^0-9]', "", price_cards_text[i].text)))
    #         price_cards_text = [int(re.sub('[^0-9]', "", text)) for text in price_cards_text]
    #         self.wait_element(CollectionLocators.PRICELIST)
    #         assert price_cards_text[i] <= price_cards_text[i+1]

    @allure.step('Добавить несколько товаров в избранное с экрана "Коллекция"')
    def add_few_to_favorite(self):
        product_list = []
        number = random.randint(0, 3)
        for i in range(number):
            self.click(CollectionLocators.FAVORITEBUTTON)
            elements_list = self.get_element(CollectionLocators.FAVORITEBUTTON).all()
            product_list.append(elements_list[i].text)
            self.swipe_page_up()
        return product_list
