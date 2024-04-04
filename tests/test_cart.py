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
        card_name = page.card.get_product_name()
        page.card.open_cart()
        page.wait_text(card_name)
        page.cart.open_card()
        page.wait_text(card_name)

    @allure.title('Экран "Корзина" / Один товар в корзине')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/29")
    @pytest.mark.smoke
    def test_one_product_in_cart(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        card_name = [page.card.get_product_name()]
        page.card.open_cart()
        page.cart.elements_full_cart()
        page.cart.checking_availability_cards(card_name)

    @allure.title('Экран "Корзина" / Несколько товаров в списке')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/587")
    @pytest.mark.smoke
    def test_one_product_in_cart(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        cards_name = [page.card.get_product_name()]
        page.press_back()
        page.press_back()
        page.add_to_cart_random_product()
        cards_name.append(page.card.get_product_name())
        page.card.open_cart()
        page.cart.checking_availability_cards(cards_name)
        page.swipe_page_up()
        page.cart.elements_full_cart()

    @allure.title('Экран "Корзина" / Изменение количества товара')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/589")
    @pytest.mark.smoke
    def test_change_quantity(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        card_price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.increasing_products_number(card_price)

    @allure.title('Экран "Корзина" / Удаление товара из корзины')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/295")
    @pytest.mark.smoke
    def test_remove_item_from_cart(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        cards_name = [page.card.get_product_name()]
        page.press_back()
        page.press_back()
        page.add_to_cart_random_product()
        cards_name.append(page.card.get_product_name())
        page.card.open_cart()
        page.cart.remove_one_item(cards_name)

    @allure.title('Экран "Корзина" / Удаление последнего товара из корзины')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/296")
    @pytest.mark.smoke
    def test_remove_last_item_from_cart(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.delete_item()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Объединение корзины при авторизации')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/340")
    @pytest.mark.smoke
    def test_merge_basket_with_authorization(self):
        page = MainPage()
        page.clear_basket()
        email = page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        cards_list = [page.card.get_product_name()]
        page.press_back()
        page.press_back()
        page.click_x()
        page.open_profile()
        page.profile.logout()
        page.click_x()
        page.open_catalog()
        page.add_to_cart_random_product()
        cards_list.append(page.card.get_product_name())
        page.press_back()
        page.press_back()
        page.click_x()
        page.login(email, valid_password2)
        page.open_cart()
        page.cart.checking_availability_cards(cards_list)

    @allure.title('Экран "Корзина" / Список товаров корзины после авторизации')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/341")
    @pytest.mark.smoke
    def test_basket_list_after_authorization(self):
        page = MainPage()
        email = page.user_registration()
        page.open_profile()
        page.profile.logout()
        page.click_x()
        page.open_catalog()
        page.add_to_cart_random_product()
        cards_list = [page.card.get_product_name()]
        page.press_back()
        page.press_back()
        page.click_x()
        page.login(email, valid_password2)
        page.open_cart()
        page.cart.checking_availability_cards(cards_list)

    @allure.title('Экран "Корзина" / Корзина после логаута')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/342")
    @pytest.mark.smoke
    def test_basket_after_logout(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.press_back()
        page.press_back()
        page.click_x()
        page.open_profile()
        page.profile.logout()
        page.click_x()
        page.open_cart()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Добавление в избранное')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/599")
    @pytest.mark.smoke
    def test_add_to_favorite_from_basket(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        cards_list = page.card.get_product_name()
        page.card.open_cart()
        page.cart.add_to_favorite()
        page.click_x()
        page.press_back()


