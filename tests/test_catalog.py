# file: test_catalog.py
import time
import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from locators import *
import allure

@pytest.mark.usefixtures("setup")
class TestAndroid:
    @allure.title('Экран "Фильтр" / Повторное применение (изменение) фильтра')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2594")
    def test_re_apply_filters(self):
        page = MainPage()
        page.click(MainLocators.banner_1)
        page.click(CollectionLocators.filters_btn)
        page.click(CollectionLocators.filter_price_asc_cbox)
        page.click(CollectionLocators.filter_apply_btn)



