from pages.main_page import MainPage
from pages.cart_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestCart:
    @allure.title('Экран "Корзина" / Пустой список')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/28")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2067")
    @pytest.mark.smoke
    def test_clear_cart(self):
        page = MainPage()
        page.clear_basket()
        page.open_cart()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Переход в каталог')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/310")
    @pytest.mark.smoke
    def test_start_shopping_btn(self):
        page = MainPage()
        page.clear_basket()
        page.open_cart()
        page.cart.click_start_shopping()

    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Переход к карточке товара')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2181")
    def test_go_to_card(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        product_name = page.card.get_product_name()
        page.card.open_cart()
        page.wait_text(product_name)
        page.cart.open_card()
        page.wait_text(product_name)

    @allure.title('Экран "Корзина" / Один товар в корзине')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/29")
    @pytest.mark.smoke
    def test_one_product_in_cart(self):
        page = MainPage()
        page.clear_basket()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.elements_full_cart()

