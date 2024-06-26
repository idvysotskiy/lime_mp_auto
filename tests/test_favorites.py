# file: test_favorites.py
import pytest

from locators import FavoritesLocators, MainLocators, CatalogLocators
from pages.main_page import MainPage
import allure
import random


@pytest.mark.usefixtures("setup")
@allure.feature("Избранное")
class TestFavorites:
    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Выход с экрана "Избранное"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/238")
    def test_exit_from_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.click(FavoritesLocators.BUTTONBACK, 'Кнопка "Назад"')
        page.wait_hidden_element(FavoritesLocators.TITLE, 'Заголовок "Избранное"')

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Экран "Избранное"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/7")
    def test_open_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Кнопка "НАЧАТЬ ПОКУПКИ')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/231")
    def test_click_bottom_buy(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.delete_from_favorites()
        page.favorites.click_pay()

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Возврат из каталога')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/277")
    def test_back_from_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.click_pay()
        page.click_x()
        page.wait_logo()

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Товар в избранном')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/8")
    def test_product_in_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.delete_from_favorites()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.wait_text(product_name)

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Удаление из избранного')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/9')
    def test_delete_from_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.delete_from_favorites()
        page.wait_hidden_element(product_name)
        page.favorites.check_empty_favorites()

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Кнопка "Купить" для товара в избранном')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/232')
    def test_bottom_buy_for_favorites_product(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.favorites_product_bottom_buy()

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Добавление товара в корзину')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/10')
    def test_add_to_cart(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = [page.card.add_to_favorites()]
        page.click_x()
        page.open_favorites()
        page.favorites.add_to_cart_and_go_to_cart()
        page.cart.checking_availability_cards(product_name)

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Переход в карточку товара и выход из нее')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/241')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/276')
    def test_go_to_card(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.go_to_card()
        page.click_x()

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Соответствие списка "Избранное" авторизованного с неавторизованным')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/278')
    def test_equals_favorite_registration_and_un_registration(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product = page.card.add_to_favorites()
        page.click_x()
        page.user_registration()
        page.open_favorites()
        favorite = page.favorites.get_text(FavoritesLocators.STUFFNAME)
        assert product == favorite

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Соответствие списка "Избранное" авторизованного с неавторизованным(Несколько товаров)')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/278')
    def test_equals_favorites_registration_and_un_registration(self, connect_to_device):
        items = [1, 2, 3, 4]
        count = random.choice(items)
        page = MainPage(connect_to_device)
        product_list = []
        page.open_catalog()
        for i in range(count):
            page.catalog.open_random_catalog()
            page.catalog.open_random_card()
            product_list = [page.card.add_to_favorites()]
            page.press_back()
            page.press_back()
        page.press_back()
        page.user_registration()
        page.open_favorites()
        page.swipe_page_up()
        favorite_list = [page.favorites.get_text(FavoritesLocators.STUFFNAME)]
        assert product_list == favorite_list

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title(' Список "Избранное" после выхода из профиля(Разлогин)')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/280')
    def test_favorite_list_after_relog(self, connect_to_device):
        items = [1, 2, 3, 4]
        count = random.choice(items)
        page = MainPage(connect_to_device)
        page.user_registration()
        page.open_catalog()
        for i in range(count):
            page.catalog.open_random_catalog()
            page.catalog.open_random_card()
            page.card.add_to_favorites()
            page.press_back()
            page.press_back()
        page.press_back()
        page.profile.logout()
        page.click_x()
        page.open_favorites()
        page.favorites.check_empty_favorites()

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title(' Экран "Избранное" / Закрыть шторку размеров (клик мимо шторки)')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/301')
    def test_close_module_screen_tap_out_range(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.favorites_product_bottom_buy()
        page.close_popup()
        page.wait_hidden_element(FavoritesLocators.MODULEWINDOW, "Модальное окно")

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Экран"Избранное" / Закрывание шторки размеров(свайп вниз)')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/302')
    def test_close_module_screen_swipe_down(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.favorites_product_bottom_buy()
        page.favorites.swipe_module_bottom()
        page.wait_a_second()
        page.wait_hidden_element(FavoritesLocators.MODULEWINDOW, "Модульное окно")

    @pytest.mark.favorites
    @pytest.mark.regress
    @allure.title('Экран "Избранное" / Четное и нечетное количество товаров в списке "Избранное"')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/333')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/334')
    def test_even_and_odd_cards_for_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        for i in range(3):
            page.catalog.open_random_catalog()
            page.catalog.open_random_card()
            page.card.add_to_favorites()
            page.press_back()
            page.press_back()
        page.click_x()
        page.open_favorites()
        page.favorites.get_cords_for_card()
