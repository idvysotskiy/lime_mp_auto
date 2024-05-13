import allure
import pytest

from config import product_name_ru
from locators import SearchLocators
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Smoke")
class TestSmoke:
    @pytest.mark.search
    @allure.title('Экран "Поиск" / Удачный поиск по текстовому запросу')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2227")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2229")
    def test_search_text(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.checking_search_elements()
        page.search.entering_search_query(product_name_ru)
        page.search.checking_elements_after_search()

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Удачный поиск по артикулу')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2230")
    def test_article_search(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.click_colors()
        article = page.card.get_article()
        page.press_back()
        page.open_search()
        page.search.entering_search_query(article)
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        page.search.open_found_card()
        page.card.checking_article_in_found_card(article)

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Добавление в избранное из результатов поиска')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2231")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2235")
    def test_adding_found_card_to_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("Платье")
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        card_name = page.search.get_card_name()
        page.search.open_found_card()
        assert card_name == page.card.get_product_name(), f"Карточка в поиске не соответствует открытой карточке. В поиске - {card_name}, открытая карточка - {page.card.get_product_name()}"
        page.card.add_to_favorites()
        page.press_back()
        page.open_favorites()
        page.favorites.checking_availability_cards(card_name)

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Добавление в избранное из результатов поиска (иконка в ячейке)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2232")
    def test_adding_found_card_to_favorites_from_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("Платье")
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        card_name = page.search.add_to_favorite()
        page.wait_a_second()
        page.click_x()
        page.open_favorites()
        page.favorites.checking_availability_cards(card_name)



