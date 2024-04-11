import random

import allure
from locators import MainLocators, ProductCardLocators, CatalogLocators, CollectionLocators
from pages.base_page import BasePage


class CatalogPage(BasePage):

    @allure.step("Переход в рандомный раздел")
    def open_random_catalog(self):
        self.wait_element(CatalogLocators.catalog_item)
        self.click(self.get_random_element_catalog(CatalogLocators.catalog_item), "рандомный раздел в меню")
        self.wait_a_moment()

        if self.get_element(CatalogLocators.catalog_item_recycler).count > 0:
            self.wait_element(MainLocators.submenu_elements_list, "подраздел каталога")
            self.click(self.get_random_element(CatalogLocators.submenu_elements_list), "рандомный подраздел каталога")

        collection_title = self.get_collection_title()
        return collection_title

    @allure.step("Переход в рандомную карточку товара")
    def open_random_card(self):
        self.wait_element(CatalogLocators.cards_image)
        self.swipe_page_up(random.randint(1, 3))
        self.wait_a_second()
        self.wait_a_second()
        self.click(self.get_random_element(CatalogLocators.cards_image), "рандомная карточка товара")
        self.wait_element(ProductCardLocators.product_name)
        product_name = self.get_text(ProductCardLocators.product_name)
        product_price = self.get_number_from_element(ProductCardLocators.product_price)
        return product_name, product_price

    @allure.step("Поиск каталога без подразделов")
    def open_catalog_without_chapter(self):
        # while True:
        #     self.wait_element(CatalogLocators.catalog_item)
        #     self.click(self.get_random_element_catalog(CatalogLocators.catalog_item), "рандомный раздел в меню")
        #     self.wait_a_moment()
        #     if self.get_element(CatalogLocators.catalog_item_recycler).count > 0:
        #         self.click_x()
        #         self.open_catalog()
        #     else:
        #         break
        while True:
            self.wait_element(CatalogLocators.catalog_item)
            counter = random.randrange(2, self.d(resourceId=CatalogLocators.catalog_item).count - 2)
            self.click(self.d(resourceId=CatalogLocators.catalog_item)[counter], "Радномный каталог")
            if self.get_element(CatalogLocators.catalog_item_recycler).count > 0:
                self.click(self.d(resourceId=CatalogLocators.catalog_item)[counter], "Закрытие подменю")
                self.wait_a_moment()
            else:
                break

    @allure.step("Получение заголовка коллекции")
    def get_collection_title(self):
        return self.get_text(CollectionLocators.title)
