import time
import allure
import pytest

from pages.base_page import BasePage
from locators import *



class FavoritesPage(BasePage):

    @allure.step("Кнопка 'Назад'")
    def click_back(self):
        self.click(FavoritesLocators.BOTTOMBACK,"Кнопка 'Назад'")
        self.(FavoritesLocators.TITLE,)

    @allure.step('Нажать кнопку "НАЧАТЬ ПОКУПКИ"')
    def click_pay(self):
        self.click(FavoritesLocators.BOTTOMBUY)
        time.sleep(10)
        self.wait_element(CatalogLocators.WOMEN,"ЖЕНЩИНЫ")
        self.wait_element(CatalogLocators.MEN,"МУЖЧИНЫ")
        self.wait_element(CatalogLocators.KIDS,"ДЕТИ")
        self.wait_element(CatalogLocators.MENU_ITEM)



