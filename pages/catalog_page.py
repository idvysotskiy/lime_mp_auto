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
            # self.wait_element(MainLocators.submenu_elements_list, "подраздел каталога")
            self.click(self.get_random_element(CatalogLocators.submenu_elements_list), "рандомный подраздел каталога")

        collection_title = self.get_collection_title()
        return collection_title

    @allure.step("Переход в раздел Футболки. Базовые модели")
    def open_shirts_page(self):
        self.wait_element(CatalogLocators.catalog_item)
        self.click(self.get_text_element("ФУТБОЛКИ"), "раздел Футболки")
        self.wait_a_moment()
        self.click(self.get_text_element("БАЗОВЫЕ"), "подраздел Базовые")

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
        while True:
            self.wait_element(CatalogLocators.catalog_item)
            counter = random.randrange(2, self.d(resourceId=CatalogLocators.catalog_item).count - 2)
            self.click(self.d(resourceId=CatalogLocators.catalog_item)[counter], "Радномный каталог")
            if self.get_element(CatalogLocators.catalog_item_recycler).count > 0:
                self.click(self.d(resourceId=CatalogLocators.catalog_item)[counter], "Закрытие подменю")
                self.wait_a_moment()
            else:
                break

    @allure.step("Поиск каталога с подразделами")
    def open_catalog_with_chapter(self):
        while True:
            self.wait_element(CatalogLocators.catalog_item)
            counter = random.randrange(2, self.d(resourceId=CatalogLocators.catalog_item).count - 2)
            name = self.get_element(CatalogLocators.catalog_item)[counter].get_text()
            self.click(self.d(resourceId=CatalogLocators.catalog_item)[counter], "Радномный каталог")
            if self.get_element(CollectionLocators.title):
                self.click_x()
                self.wait_a_moment()
            else:
                break
        return name

    @allure.step("Получение заголовка коллекции")
    def get_collection_title(self):
        return self.get_text(CollectionLocators.title)

    def click_catalog_coords(self):
        bounds = self.get_random_element_catalog(CatalogLocators.catalog_item).bounds()
        self.coordinate_click(bounds[2] - 100, (bounds[3] + bounds[1]) / 2)

    @allure.step('Поиск экрана коллекции с баннером')
    def open_collection_with_banner(self):
        for i in range(self.get_element(CatalogLocators.catalog_item).count):
            elements = self.get_element("//*[@resource-id='ru.limeshop.android.dev:id/catalog_item_name']").all()
            self.click(elements[i], elements[i].text)
            self.wait_a_moment()

            if self.get_element(CatalogLocators.catalog_item_recycler).count > 0:
                self.wait_element(MainLocators.submenu_elements_list, "подраздел каталога")
                self.click(CatalogLocators.submenu_elements_list, "первый подраздел каталога")

            if self.get_element(CollectionLocators.banner_image).count > 0:
                return

            self.click_x()
