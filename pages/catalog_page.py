import allure
from locators import MainLocators, ProductCardLocators, CatalogLocators
from pages.base_page import BasePage


class CatalogPage(BasePage):

    @allure.step("Переход в рандомный раздел")
    def open_random_catalog(self):
        self.wait_element(CatalogLocators.catalog_item)
        self.click(self.get_random_element(CatalogLocators.catalog_item), "рандомный раздел в меню")
        self.wait_a_moment()

        if self.get_element(CatalogLocators.catalog_item_recycler).count > 0:
            self.wait_element(MainLocators.submenu_elements_list, "подраздел каталога")
            self.click(self.get_random_element(CatalogLocators.submenu_elements_list), "рандомный подраздел каталога")

    @allure.step("Переход в рандомную карточку товара")
    def open_random_card(self):
        self.swipe_page_up(3)
        self.click(CatalogLocators.cards_image, "рандомная карточка товара")
        self.wait_element(ProductCardLocators.product_name)
        product_name = self.get_text(ProductCardLocators.product_name)
        product_price = self.get_number_from_element(ProductCardLocators.product_price)
        return product_name, product_price
