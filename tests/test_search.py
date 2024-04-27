# file: test_search.py
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
    @allure.testcase("C3")
    def test_search_text(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.search.go_to_search()
        page.search.elements_search_first()
        page.search.search(product_name_ru)
        page.search.elements_search()

    @pytest.mark.search
    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Валидный запрос для одной категории')
    @allure.testcase("C1779")
    def test_search_text_one_category(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.search.go_to_search()
        page.search.elements_search_first()
        page.search.search(product_name_ru)
        page.search.elements_search()
        page.click(SearchLocators.MEN)
        page.search.elements_search_fail()

    @pytest.mark.search
    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Удачный поиск по артикулу')
    @allure.testcase("C199")
    def test_search_article(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.search.go_to_search()
        page.search.elements_search_first()
        page.search.search(product_article)
        page.search.elements_search()
