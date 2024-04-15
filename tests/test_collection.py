import time

import pytest

from locators import FavoritesLocators, MainLocators, CatalogLocators, CollectionLocators
from pages.main_page import MainPage
import allure
import random


@pytest.mark.usefixtures("setup")
@allure.feature("Коллекция")
class TestCollection:

    @pytest.mark.catalog
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Коллекции" / Переход на экран')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/483")
    def test_open_collection(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.collection.click_x()
        page.wait_element(CatalogLocators.catalog_item)
        page.catalog.wait_element(CatalogLocators.WOMEN)
        page.catalog.wait_element(CatalogLocators.MEN)
        page.catalog.wait_element(CatalogLocators.KIDS)
