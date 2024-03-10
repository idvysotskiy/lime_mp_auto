import time
import allure
from pages.base_page import BasePage
from locators import *
from config import *

X_BUTTON = '//android.widget.ImageButton'
TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/toolbarTitle"]'
TEXT_EDIT = '//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
TEXT_HINT = '//*[@resource-id="ru.limeshop.android.dev:id/hintText"]'
ICON = '//*[@resource-id="ru.limeshop.android.dev:id/startIcon"]'
SHOPS_BTN = '//*[@resource-id="ru.limeshop.android.dev:id/topButtonsContainerLinearLayout"]/androidx.appcompat.widget.LinearLayoutCompat[1]'
SCAN_BTH = '//*[@resource-id="ru.limeshop.android.dev:id/topButtonsContainerLinearLayout"]/androidx.appcompat.widget.LinearLayoutCompat[2]'
SHOPS_TEXT = '//*[@text="МАГАЗИНЫ"]'
SCAN_TEXT = '//*[@text="СКАНЕР"]'
ALL = '//*[@text="ВСЕ"]'
WOMAN = '//*[@text="ЖЕНЩИНЫ"]'
MEN = '//*[@text="МУЖЧИНЫ"]'
KIDS = '//*[@text="ДЕТИ"]'
FIRST_RESULT_IMAGE = '//*[@resource-id="ru.limeshop.android.dev:id/searchRecyclerView"]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]'
FIRST_RESULT_NAME = '"ru.limeshop.android.dev:id/item_product_name", text="ПЛАТЬЕ ИЗ АТЛАСА С ПРИНТОМ «ЖЕМЧУГ»"'
FIRST_RESULT_FAV = '//*[@resource-id="ru.limeshop.android.dev:id/searchRecyclerView"]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
ICON_FAIL_SEARCH = '//androidx.appcompat.widget.LinearLayoutCompat/android.widget.ImageView[1]'
FAIL_SEARCH_TEXT = '//*[@text="НИЧЕГО НЕ НАЙДЕНО"]'
FAIL_SEARCH_DESCRIPTION = '//*[@text="Проверьте, правильно ли введен запрос"]'

class SearchPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

    @allure.step('Нажать кнопку "Поиск"')
    def go_to_search(self):
        self.click(MainLocators.SEARCH_NAV)

    @allure.title('Экран "Поиск" / Первый переход на экран "Поиск"')
    @allure.testcase("C60")
    def elements_search_first(self):
        assert self.get_text(TITLE) == 'ПОИСК'
        self.is_element_present(X_BUTTON)
        assert self.get_text(TEXT_HINT) == 'Введите название или артикул'
        assert self.get_text(SHOPS_TEXT) == 'МАГАЗИНЫ'
        assert self.get_text(SCAN_TEXT) == 'СКАНЕР'

    @allure.step('Ввести запрос в поле "Поиск"')
    def search(self, text):
        self.set_text(TEXT_EDIT, text)
        assert self.get_text(TEXT_EDIT) == text

    @allure.step('Проверка элементов на экране после ввода запроса поиска')
    def elements_search(self):
        assert self.get_text(TITLE) == 'ПОИСК'
        self.is_element_present(X_BUTTON)
        assert self.get_text(ALL) == 'ВСЕ'
        assert self.get_text(WOMAN) == 'ЖЕНЩИНЫ'
        assert self.get_text(MEN) == 'МУЖЧИНЫ'
        assert self.get_text(KIDS) == 'ДЕТИ'

    @allure.step('Проверка элементов на экране после неудачного поиска')
    def elements_search_fail(self):
        assert self.get_text(FAIL_SEARCH_TEXT) == 'НИЧЕГО НЕ НАЙДЕНО'
        assert self.get_text(FAIL_SEARCH_DESCRIPTION) == 'Проверьте, правильно ли введен запрос'