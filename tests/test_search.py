# file: test_search.py
import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
from pages.search_pages import *
import allure

@pytest.mark.usefixtures("setup")
class TestAndroid:
    @allure.title('Экран "Поиск" / Удачный поиск по текстовому запросу')
    @allure.testcase("C3")
    def test_search_text(self):
        page = SearchPage()
        page.go_to_search()
        page.elements_search_first()
        page.search('платье')
        page.elements_search()

    @allure.title('Экран "Поиск" / Валидный запрос для одной категории')
    @allure.testcase("C1779")
    def test_search_text_one_category(self):
        page = SearchPage()
        page.go_to_search()
        page.elements_search_first()
        page.search('платье')
        page.elements_search()
        page.click(MEN)
        page.elements_search_fail()

    @allure.title('Экран "Поиск" / Удачный поиск по артикулу')
    @allure.testcase("C199")
    def test_search_article(self):
        page = SearchPage()
        page.go_to_search()
        page.elements_search_first()
        page.search('0377-454')
        page.elements_search()
