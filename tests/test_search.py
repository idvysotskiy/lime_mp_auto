import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Поиск")
class TestSearch:
    @pytest.mark.search
    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Удачный поиск по текстовому запросу')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/60")
    def test_search_text(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.checking_search_elements()
        page.search.entering_search_query(product_name_ru)
        page.search.checking_elements_after_search()

    @pytest.mark.search
    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Удачный поиск по артикулу')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/199")
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

    @pytest.mark.search
    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Артикул для разных категорий')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1778")
    def test_articles_for_different_categories(self, connect_to_device):
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
        page.search.open_tab("МУЖЧИНЫ")
        page.search.checking_empty_search_page()
        page.search.open_tab("ДЕТИ")
        page.search.checking_empty_search_page()
        page.search.open_tab("ВСЕ")
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")

    @pytest.mark.search
    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Валидный запрос для одной категории')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1779")
    def test_valid_query_for_one_category(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("Платье")
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        page.search.open_tab("МУЖЧИНЫ")
        page.search.checking_empty_search_page()

    @pytest.mark.search
    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Неудачный поиск + переход по категориям')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/5")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1777")
    def test_unsuccessful_search(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("Фуфайка")
        page.search.checking_empty_search_page()
        page.search.open_tab("МУЖЧИНЫ")
        page.search.checking_empty_search_page()
        page.search.open_tab("ДЕТИ")
        page.search.checking_empty_search_page()
        page.search.open_tab("ВСЕ")
        page.search.checking_empty_search_page()

    @pytest.mark.search
    @pytest.mark.regress
    @allure.title('Экран "Поиск" / Добавление в избранное из результатов поиска')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/6")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/433")
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

    @pytest.mark.search
    @pytest.mark.regress
    @allure.title('Экран "Поиск" / Добавление в избранное из результатов поиска (иконка в ячейке)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/268")
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

    @pytest.mark.search
    @pytest.mark.regress
    @allure.title('Экран "Поиск" / Экран поиска с историей поиска')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/267")
    def test_search_history(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        search_query = "Платье"
        page.search.entering_search_query(search_query)
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        page.click_x()
        page.open_search()
        page.search.checking_search_history(search_query)

    @pytest.mark.search
    @pytest.mark.regress
    @allure.title('Экран "Поиск" / Экран поиска с историей поиска')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/200")
    def test_delete_favorite_from_search(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        card_name = page.card.get_product_name()
        page.card.click_colors()
        article = page.card.get_article()
        page.press_back()
        page.open_search()
        page.search.entering_search_query(article)
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        page.search.delete_favorite_card(card_name)
        page.click_x()
        page.open_favorites()
        page.favorites.check_empty_favorites()

    @pytest.mark.search
    @pytest.mark.regress
    @allure.title('Экран "Поиск" / Поиск по вводу пробела')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1908")
    def test_search_space_query(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("  ")
        page.wait_hidden_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")

    @pytest.mark.search
    @pytest.mark.regress
    @allure.title('Экран "Поиск" / Поиск по вводу спец символов')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/45154")
    def test_search_symbols_query(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("#@&")
        page.search.checking_empty_search_page()
