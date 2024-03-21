import allure
from pages.base_page import BasePage


class FavoritesPage(BasePage):
    @allure.step('Шаблончик')
    def print_test(self):
        print('test')


