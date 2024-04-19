import time

import pytest

from locators import FavoritesLocators, MainLocators, CatalogLocators, CollectionLocators
from pages.main_page import MainPage
import allure
import random


@pytest.mark.usefixtures("setup")
@allure.feature("Коллекция")
class TestCollection:

    @pytest.mark.collection
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Коллекции" / Выход с экрана')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/3391')
    def test_close_collection(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.collection.click_x()
        page.wait_element(CatalogLocators.catalog_item)
        page.catalog.wait_element(CatalogLocators.WOMEN)
        page.catalog.wait_element(CatalogLocators.MEN)
        page.catalog.wait_element(CatalogLocators.KIDS)

    @pytest.mark.collection
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Коллекция" / Переход на экран "Коллекция"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/483")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/484")
    def test_open_collection(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.wait_element(CollectionLocators.title)
        page.catalog.wait_element(CollectionLocators.cards_image)
        page.catalog.wait_element(CollectionLocators.filters_btn)

    @pytest.mark.collection
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Коллекции" / Баннер в коллекции (клик на баннер)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/336")
    def test_click_banner(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_collection_with_banner()
        page.collection.click(CollectionLocators.banner_image)
        page.collection.wait_hidden_element(CollectionLocators.banner_image)

    # @pytest.mark.collection
    # @pytest.mark.smoke
    # @pytest.mark.regress
    # @allure.title('Экран "Коллекции" / Сортировка коллекции')
    # @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/171")
    # def test_sort_cards(self):
    #     page = MainPage()
    #     page.open_catalog()
    #     page.catalog.open_random_catalog()
    #     page.collection.click(CollectionLocators.filters_btn)
    #     page.collection.sort_upper_price()

    @pytest.mark.collection
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Коллекции" / Переход к карточке товара')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/286")
    def test_open_card(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()

    @pytest.mark.collection
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Коллекции" / Добавление в избранное (добавление в список) с экрана "Коллекция"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/283")
    def test_add_to_favorites(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.swipe_page_up()
        # page.collection.add_to_favorite()
        product_name = page.collection.add_to_favorite()
        page.open_favorites()
        favorites_product = page.favorites.get_text(FavoritesLocators.STUFFNAME)
        assert product_name == favorites_product, 'Товары разные!!'

    @pytest.mark.collection
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Коллекции" / Добавление в избранное (добавление в список) с экрана "Коллекция"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/283")
    def test_delete_favorites_from_collection(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        product_card = page.collection.add_to_favorite()
        page.open_favorites()
        page.open_catalog()
        page.collection.add_to_favorite(product_card)
        page.open_favorites()
        page.wait_element(FavoritesLocators.BUTTONBUY)
        page.wait_element(FavoritesLocators.INFOTEXT)

    @pytest.mark.collection
    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Коллекции" / Добавление в избранное нескольких товаров (более 3-х) с экрана "Коллекция"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3101")
    def test_add_few_favorites_from_collection(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.collection.add_few_to_favorite()
        product_list = page.get_text(CollectionLocators.CARDNAME)
        page.open_favorites()
        favorite_list = page.get_text(FavoritesLocators.STUFFNAME)
        assert favorite_list == product_list
