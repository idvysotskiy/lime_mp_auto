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
                self.wait_element(CatalogLocators.submenu_elements_list, "подраздел каталога")
                self.click(CatalogLocators.submenu_elements_list, "первый подраздел каталога")

            if self.get_element(CollectionLocators.banner_image).count > 0:
                return

            self.click_x()

    @allure.step('Переключение между разделами')
    def change_chapter(self):
        list_of_elements = []
        elements = self.get_element(CatalogLocators.catalog_item)
        for i in range(self.get_elements_amount(CatalogLocators.catalog_item)):
            list_of_elements.append(elements[i].get_text())
        print(elements)
        chapter = random.choice((CatalogLocators.KIDS, CatalogLocators.MEN))
        print("Выбранный раздел" + chapter)
        self.click(chapter)
        list_of_elements2 = []
        elements2 = self.get_element(CatalogLocators.catalog_item)
        for i in range(self.get_elements_amount(CatalogLocators.catalog_item)):
            list_of_elements2.append(elements2[i].get_text())
        print(elements2)
        assert list_of_elements != list_of_elements2, print("Разделы  не отличаются")

    @allure.step('Добавление в избранное из каталога')
    def add_to_favorites_from_catalog(self):
        self.click(CollectionLocators.FAVORITEBUTTON)
        product_name = self.get_text(CollectionLocators.CARDNAME)
        product_price = self.get_number_from_element(CollectionLocators.CARDPRICE)
        return product_price, product_name

    @allure.step('Добавление в избранное из каталога')
    def add_a_few_to_favorites_from_catalog(self):
        product_name_list = []
        number = [1, 2, 3]
        c = random.choice(number)
        for i in range(c):
            self.click(CollectionLocators.FAVORITEBUTTON)
            product_name = self.get_text(CollectionLocators.CARDNAME)
            product_name_list.append(product_name)
            self.swipe_page_up()
            self.swipe_page_up()
        return product_name_list

    @allure.step('Переход в карточку товара')
    def open_card(self):
        self.swipe_page_up()
        self.swipe_page_up()
        self.click(CollectionLocators.cards_image)

    @allure.step('Комбинированная фильтрация')
    def combine_filtration(self):
        number = [0, 1]
        random.choice(number)
        if number == 1:
            self.click(CollectionLocators.filter_price_asc_cbox)
        else:
            self.click(CollectionLocators.filter_price_desc_cbox)
        box_list = self.get_element(CollectionLocators.CHECKBOX_FILTERS).count
        for i in range(box_list):
            a = random.choice(box_list)
            self.click(CollectionLocators.CHECKBOX_FILTERS(a))
        self.swipe_page_up()
        self.swipe_page_up()