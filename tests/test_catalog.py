import time

import pytest

from locators import FavoritesLocators, MainLocators, CatalogLocators, CollectionLocators
from pages.main_page import MainPage
import allure
import random


@pytest.mark.usefixtures("setup")
@allure.feature("Каталог")
class TestCatalog:
    @pytest.mark.catalog
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Каталог" / Переход из каталога на основной экран')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1757")
    def test_close_catalog(self):
        page = MainPage()
        page.open_catalog()
        page.click_x()
        page.wait_hidden_element(CatalogLocators.catalog_item)
        page.wait_element(MainLocators.lime_logo)
        page.wait_hidden_element(CatalogLocators.MENU_ITEM)

    @pytest.mark.catalog
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Каталог" / Основной раздел')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/53")
    def test_open_catalog(self):
        page = MainPage()
        page.open_catalog()
        page.wait_element(CatalogLocators.WOMEN)
        page.wait_element(CatalogLocators.KIDS)
        page.wait_element(CatalogLocators.MEN)
        page.wait_element(MainLocators.X_BUTTON, 'Кнопка "Назад"')
        catalog_list = page.catalog.get_element(CatalogLocators.catalog_item).count
        assert catalog_list >= 1, print(f"Разделы каталогов не найдены. Catalog_list = {catalog_list}")
        page.swipe_page_up()
        page.wait_element(CatalogLocators.GIFT_CARD, 'Подарочная карта')

    @pytest.mark.catalog
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Каталог" / Раздел без подразделов')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/54")
    def test_catalog_without_chapter(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_catalog_without_chapter()

    @pytest.mark.catalog
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Каталог" / Переход от раздела к разделу(Содержащий подразделы)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/54")
    def test_catalog_with_chapter(self):
        page = MainPage()
        page.open_catalog()
        catalog_name = page.catalog.open_catalog_with_chapter()
        print(f"{catalog_name}.Содержит разделы")

    @pytest.mark.catalog
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Каталог" / Клик по ячейке пункта меню')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/3221")
    def test_tap_out_name_catalog(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.click_catalog_coords()
        if page.catalog.get_element(CatalogLocators.catalog_item_recycler).count == 0:
            page.wait_element(CollectionLocators.title)





