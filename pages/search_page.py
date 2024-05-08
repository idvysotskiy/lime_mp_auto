import allure
from pages.base_page import BasePage
from locators import *


class SearchPage(BasePage):
    @allure.step('Проверка элементов поиска')
    def checking_search_elements(self):
        self.wait_element(SearchLocators.TITLE, "заголовок Поиск")
        self.wait_element(SearchLocators.X_BUTTON, "кнопка Закрыть")
        self.wait_element(SearchLocators.TEXT_HINT, "подсказка для поля поиска")
        self.wait_element(SearchLocators.SHOPS_TEXT, "кнопка Магазины")
        self.wait_element(SearchLocators.SCAN_TEXT, "кнопка Сканер")
        self.wait_hidden_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")

    @allure.step('Ввод запрос в поле "Поиск"')
    def entering_search_query(self, text):
        self.set_text(SearchLocators.TEXT_EDIT, text)
        assert self.get_text(SearchLocators.TEXT_EDIT) == text

    @allure.step('Проверка элементов на экране после ввода запроса поиска')
    def checking_elements_after_search(self):
        self.wait_element(SearchLocators.TITLE, "заголовок Поиск")
        self.wait_element(SearchLocators.X_BUTTON, "кнопка Закрыть")
        self.wait_element(SearchLocators.ALL, "кнопка Все")
        self.wait_element(SearchLocators.WOMAN, "кнопка Женщины")
        self.wait_element(SearchLocators.MEN, "кнопка Мужчины")
        self.wait_element(SearchLocators.KIDS, "кнопка Дети")
        self.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")

    @allure.step('Проверка элементов на экране после неудачного поиска')
    def elements_search_fail(self):
        assert self.get_text(SearchLocators.FAIL_SEARCH_TEXT) == 'НИЧЕГО НЕ НАЙДЕНО'
        assert self.get_text(SearchLocators.FAIL_SEARCH_DESCRIPTION) == 'Проверьте, правильно ли введен запрос'

    @allure.step("Переход в найденную карточку")
    def open_found_card(self):
        self.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        self.click(SearchLocators.card_img_in_search_result, "найденная карточка")

    @allure.step("Переход в категорию '{tab_name}'")
    def open_tab(self, tab_name):
        self.click(f'//*[@text="{tab_name}"]', f"категория {tab_name}")

    @allure.step("Проверка пустой страницы поиска")
    def checking_empty_search_page(self):
        self.wait_text("НИЧЕГО НЕ НАЙДЕНО")
        self.wait_text("Проверьте, правильно ли введен запрос")

    # @allure.step("Получение названия карточки")
    def get_card_name(self):
        return self.get_text(SearchLocators.card_name_in_search_result)

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.click(SearchLocators.card_favorite_icon, "иконка добавления в избранное")
        return self.get_text(SearchLocators.card_name_in_search_result)

    @allure.step("Проверка наличия в истории поиска строки '{history_item}'")
    def checking_search_history(self, history_item):
        self.wait_text("НЕДАВНИЕ")
        self.wait_element(f'//*[@resource-id="ru.limeshop.android.dev:id/search_history_recycler"]/*[@text="{history_item}"]', f"'{history_item}' в истории поиска")

    @allure.step("Удаление из избранного в поиске карточки '{card_name}'")
    def delete_favorite_card(self, card_name):
        self.click(f'//*[@resource-id="ru.limeshop.android.dev:id/item_product_name" and @text="{card_name}"]/following-sibling::*[@resource-id="ru.limeshop.android.dev:id/item_product_favorite"]')