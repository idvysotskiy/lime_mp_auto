# file: test_favorites.py
import pytest
from pages.main_page import MainPage
import allure


@pytest.mark.usefixtures("setup")
class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Кнопка "НАЧАТЬ ПОКУПКИ')
    @allure.testcase("")
    def test_example(self):
        page = MainPage()
        page.open_favorites()
        page.favorites.click_pay()



