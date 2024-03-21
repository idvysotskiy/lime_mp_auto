import time
import allure
import pytest

from pages.base_page import BasePage
from locators import *



class FavoritesPage(BasePage):

    def open_favorites(self):
        self.click(MainLocators.FAVORITES_NAV)
        self.wait_element(FavoritesLocators.TITLE)
        self.wait_element(FavoritesLocators.BOTTOMBUY)
        self.wait_text("НАЧАТЬ ПОКУПКИ")
        self.wait_text("ВАШ ВИШЛИСТ ПУСТ")
        # button_text = self.get_text(FavoritesLocators.BOTTOMBUY)
        # assert button_text == "НАЧАТЬ ПОКУПКИ123", print(f"Текст отличается от макета. Текст в приложении {button_text}, а мы ожидали 'НАЧАТЬ ПОКУПКИ123'")
