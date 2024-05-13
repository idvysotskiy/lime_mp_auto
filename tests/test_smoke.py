import allure
import pytest

from config import product_name_ru
from locators import SearchLocators, FavoritesLocators
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Smoke")
class TestSmoke:
    @pytest.mark.search
    @allure.title('Экран "Поиск" / Удачный поиск по текстовому запросу')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2227")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2229")
    def test_search_text(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.checking_search_elements()
        page.search.entering_search_query(product_name_ru)
        page.search.checking_elements_after_search()

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Удачный поиск по артикулу')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2230")
    def test_article_search(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.click_colors()
        article = page.card.get_article()
        page.press_back()
        page.open_search()
        page.search.entering_search_query(article)
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        page.search.open_found_card()
        page.card.checking_article_in_found_card(article)

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Добавление в избранное из результатов поиска')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2231")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2235")
    def test_adding_found_card_to_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("Платье")
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        card_name = page.search.get_card_name()
        page.search.open_found_card()
        assert card_name == page.card.get_product_name(), f"Карточка в поиске не соответствует открытой карточке. В поиске - {card_name}, открытая карточка - {page.card.get_product_name()}"
        page.card.add_to_favorites()
        page.press_back()
        page.open_favorites()
        page.favorites.checking_availability_cards(card_name)

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Добавление в избранное из результатов поиска (иконка в ячейке)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2232")
    def test_adding_found_card_to_favorites_from_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("Платье")
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        card_name = page.search.add_to_favorite()
        page.wait_a_second()
        page.click_x()
        page.open_favorites()
        page.favorites.checking_availability_cards(card_name)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Пустой список')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2236")
    def test_empty_favorites_screen(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.wait_element(FavoritesLocators.BUTTONBUY)
        page.favorites.wait_element(FavoritesLocators.INFOTEXT)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Товар в избранном')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2237")
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
        page.wait_element(FavoritesLocators.BUTTONBUYSTUFF)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Удаление товара из избранного')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2238")
    def test_delete_product_from_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.delete_from_favorites()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.click(FavoritesLocators.BOTTONDELETEFROMFAV)
        page.wait_a_second()
        page.favorites.wait_hidden_element(FavoritesLocators.BUTTONBUYSTUFF)
        page.favorites.wait_element(FavoritesLocators.INFOTEXT)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Кнопка "Купить" для товара')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/2239')
    def test_bottom_buy_for_favorites_product(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.favorites_product_bottom_buy()

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Добавить товар в корзину')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/2240')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/2241')
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

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Переход на экран "Корзина"(Через ТапБар)')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/2242')
    def test_add_to_cart_from_navbar(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = [page.card.add_to_favorites()]
        page.click_x()
        page.open_favorites()
        page.favorites.add_to_cart()
        page.open_cart()
        page.cart.checking_availability_cards(product_name)




