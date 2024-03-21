# file: test_favorites.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Шаблон')
    @allure.testcase("")
    def test_example(self):
        print('test')


