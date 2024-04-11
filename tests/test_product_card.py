# file: test_product_card.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Карточка товара")
class TestMobile:
    @allure.title('Экран "Карточка товара" / Кнопка "Купить"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/12")
    @pytest.mark.smoke
    def test_size_bottom_sheet(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_cart()
        page.wait_element(FavoritesLocators.MODULEWINDOW, "Модальное окно")
        page.wait_element(FavoritesLocators.SIZEINSTUCTION, "Руководство по размерам")
        page.wait_element(FavoritesLocators.SIZE, "Размер")

    @allure.title('Экран "Карточка товара" / Открыть карточку товара')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/288")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/290")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/11")
    @pytest.mark.smoke
    def test_open_product_card(self):
        page = MainPage()
        page.open_catalog()
        collection_title = page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.checking_card_elements()
        page.card.click_back()
        assert collection_title == page.catalog.get_collection_title(), print(f"Название коллекции после возврата из карточки изменилось. До переход в карточку: {collection_title}, после перехода: {page.catalog.get_collection_title()}")

    @allure.title('Экран "Карточка товара" / Кнопка Купить (Изменение)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1622")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1979")
    @pytest.mark.smoke
    def test_buy_button_changes(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.wait_element(ProductCardLocators.BUY_MORE, "кнопка Купить еще")
        page.card.open_cart()
        page.cart.cart_clear()
        page.click_x()
        page.wait_element(ProductCardLocators.BUY, "кнопка Купить")

    @allure.title('Экран "Карточка товара" / Кнопка Избранное (Добавить в избранное)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/291")
    @pytest.mark.smoke
    @pytest.mark.regress
    def test_add_to_favorites(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.wait_text(product_name)

    @allure.title('Экран "Карточка товара" / Кнопка Избранное (Удалить из избранного)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/293")
    @pytest.mark.smoke
    @pytest.mark.regress
    def test_delete_from_favorites(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.check_empty_favorites()

    @allure.title('Экран "Карточка товара" / Кнопка Поделиться')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/13")
    @pytest.mark.smoke
    @pytest.mark.regress
    def test_share(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.click_share()
        page.wait_text("SHARE")

    @allure.title('Экран "Карточка товара" / Кнопка Корзина')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/294")
    @pytest.mark.smoke
    def test_basket_button(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.check_empty_cart()

    @allure.title('Экран "Карточка товара" / Кнопка Доставка и возврат')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3123")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3126")
    @pytest.mark.smoke
    def test_delivery_button(self):
        page = MainPage()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.swipe_in_card()
        page.card.click_delivery()
        page.swipe_page_down()
        page.wait_hidden_element(ProductCardLocators.delivery_description_page, "описание доставки и возврата")




    # @pytest.mark.smoke
    # @allure.title('')
    # @allure.testcase("")
    # def test_buy_wtf(self):
    #     page = MainPage()
    #     page.clear_basket()
    #     page.open_catalog()
    #     page.catalog.open_random_catalog()
    #     page.catalog.open_random_card()
    #     page.card.elements_product_card()
    #     page.card.open_full_product_card()
    #     page.card.elements_full_product_card()
