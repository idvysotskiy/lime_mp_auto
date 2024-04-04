import time
import allure
import pytest

from pages.base_page import BasePage
from locators import *


class FavoritesPage(BasePage):

    @allure.step("Экран 'Избранное'")
    @allure.step("Кнопка 'Назад'")
    def click_back(self):
        self.click(FavoritesLocators.BOTTOMBACK, "Кнопка 'Назад'")
        self.wait_hidden_element(FavoritesLocators.TITLE, "ЗАГОЛОВОК")
        self.wait_hidden_element(FavoritesLocators.BOTTOMBUY, "Кнопка 'НАЧАТЬ ПОКУПКИ'")

    @allure.step('Нажать кнопку "НАЧАТЬ ПОКУПКИ"')
    def click_pay(self):
        self.click(FavoritesLocators.BOTTOMBUY)
        time.sleep(10)
        self.wait_element(CatalogLocators.WOMEN, "ЖЕНЩИНЫ")
        self.wait_element(CatalogLocators.MEN, "МУЖЧИНЫ")
        self.wait_element(CatalogLocators.KIDS, "ДЕТИ")
        self.wait_element(CatalogLocators.MENU_ITEM)

    @allure.step('Удалить все товары из Избранного')
    def delete_from_favorites(self):
        while len(self.get_element(FavoritesLocators.BOTTOMBUYSTUFF).all()) > 0:
            self.click(FavoritesLocators.BOTTOMFAVORITES, 'Кнопка "Добавить/Убрать в избранное"')
            self.wait_a_second()

    @allure.step("Проверка пустого избранного")
    def check_empty_favorites(self):
        self.wait_element(FavoritesLocators.INFOTEXT,"ВАШ ВИШЛИСТ ПУСТ")
        self.wait_element(FavoritesLocators.BOTTOMBUY, 'Кнопка "НАЧАТЬ ПОКУПКИ')

    @allure.step("Открытие модального окна")
    def favorites_product_bottom_buy(self):
        self.click(FavoritesLocators.BOTTOMBUYSTUFF, 'Кнопка "Купить" для товара')
        self.wait_element(FavoritesLocators.MODULEWINDOW, "Модальное окно")
        self.wait_element(FavoritesLocators.SIZEINSTUCTION, "Руководство по размерам")
        self.wait_element(FavoritesLocators.SIZE, "Размер")

    @allure.step("Добавление в корзину")
    def add_favorite_product_to_cart(self):


