import allure
from pages.base_page import BasePage
from locators import *


class SearchPage(BasePage):

    @allure.step('Нажать кнопку "Поиск"')
    def go_to_search(self):
        self.click(MainLocators.SEARCH_NAV)

    @allure.title('Экран "Поиск" / Первый переход на экран "Поиск"')
    @allure.testcase("C60")
    def elements_search_first(self):
        assert self.get_text(SearchLocators.TITLE) == 'ПОИСК'
        self.is_element_present(SearchLocators.X_BUTTON)
        assert self.get_text(SearchLocators.TEXT_HINT) == 'Введите название или артикул'
        assert self.get_text(SearchLocators.SHOPS_TEXT) == 'МАГАЗИНЫ'
        assert self.get_text(SearchLocators.SCAN_TEXT) == 'СКАНЕР'

    @allure.step('Ввести запрос в поле "Поиск"')
    def search(self, text):
        self.set_text(SearchLocators.TEXT_EDIT, text)
        assert self.get_text(SearchLocators.TEXT_EDIT) == text

    @allure.step('Проверка элементов на экране после ввода запроса поиска')
    def elements_search(self):
        assert self.get_text(SearchLocators.TITLE) == 'ПОИСК'
        self.is_element_present(SearchLocators.X_BUTTON)
        assert self.get_text(SearchLocators.ALL) == 'ВСЕ'
        assert self.get_text(SearchLocators.WOMAN) == 'ЖЕНЩИНЫ'
        assert self.get_text(SearchLocators.MEN) == 'МУЖЧИНЫ'
        assert self.get_text(SearchLocators.KIDS) == 'ДЕТИ'

    @allure.step('Проверка элементов на экране после неудачного поиска')
    def elements_search_fail(self):
        assert self.get_text(SearchLocators.FAIL_SEARCH_TEXT) == 'НИЧЕГО НЕ НАЙДЕНО'
        assert self.get_text(SearchLocators.FAIL_SEARCH_DESCRIPTION) == 'Проверьте, правильно ли введен запрос'
