import pytest

from locators import FavoritesLocators, MainLocators, CatalogLocators, CollectionLocators
from pages.main_page import MainPage
import allure
import random


@pytest.mark.usefixtures("setup")
class TestAndroid:

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

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Каталог" / Раздел без подразделов')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/54")
    def test_catalog_without_chapter(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_catalog_without_chapter()
        catalog_name = page.get_text(CollectionLocators.tittle)
        print(catalog_name, f"{catalog_name} не имеет подразделов")

