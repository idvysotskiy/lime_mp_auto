# file: test_favorites.py
import pytest

from locators import FavoritesLocators
from pages.main_page import MainPage
import allure


@pytest.mark.usefixtures("setup")
class TestAndroid:

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Экран "Избранное"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/7")
    def test_open_favorites(self):
        page = MainPage()
        page.open_favorites()

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Кнопка "НАЧАТЬ ПОКУПКИ')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/231")
    def test_click_bottom_buy(self):
        page = MainPage()
        page.open_favorites()
        page.favorites.click_pay()

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Возврат из каталога')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/277")
    def test_back_from_catalog(self):
        page = MainPage()
        page.open_favorites()
        page.favorites.click_pay()
        page.click_x()
        page.wait_logo()

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Товар в избранном')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/8")
    def test_product_in_favorites(self):
        page = MainPage()
        page.open_favorites()
        page.favorites.delete_from_favorites()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = page.card.add_to_favorites()
        page.press_back()
        page.open_favorites()
        page.wait_text(product_name)

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Удаление из избранного')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/9')
    def test_delete_from_favorites(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = page.card.add_to_favorites()
        page.press_back()
        page.open_favorites()
        page.favorites.delete_from_favorites()
        page.wait_hidden_element(product_name)
        page.favorites.check_empty_favorites()

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Кнопка "Купить" для товара в избранном')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/232')
    def test_bottom_buy_for_favorites_product(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.press_back()
        page.open_favorites()
        page.favorites.favorites_product_bottom_buy()

    @pytest.mark.smoke
    @pytest.mark.regress
    @allure.title('Добавление товара в корзину')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/10')
    def add_to_cart(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.press_back()
        page.open_favorites()
        page.favorites.favorites_product_bottom_buy()
        page.click(FavoritesLocators.SIZE)
        page.open_cart()


