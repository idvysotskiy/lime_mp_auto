from pages.main_page import MainPage
from pages.cart_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestCart:
    @allure.title('Экран "Корзина" / Пустой список. Кнопка "Очистить" для пустой корзины')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/28")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2067")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_clear_cart(self):
        page = MainPage()
        page.clear_basket()
        page.open_cart()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Переход в каталог')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/310")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_start_shopping_btn(self):
        page = MainPage()
        page.clear_basket()
        page.open_cart()
        page.cart.click_start_shopping()

    @allure.title('Экран "Корзина" / Переход к карточке товара')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2181")
    @pytest.mark.basket
    @pytest.mark.smoke
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
    @pytest.mark.basket
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
    @pytest.mark.basket
    def test_several_product_in_cart(self):
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
    @pytest.mark.basket
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
    @pytest.mark.basket
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
    @pytest.mark.basket
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
    @pytest.mark.basket
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
        page.login(email, valid_password)
        page.open_cart()
        page.cart.checking_availability_cards(cards_list)

    @allure.title('Экран "Корзина" / Список товаров корзины после авторизации')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/341")
    @pytest.mark.smoke
    @pytest.mark.basket
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
        page.login(email, valid_password)
        page.open_cart()
        page.cart.checking_availability_cards(cards_list)

    @allure.title('Экран "Корзина" / Корзина после логаута')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/342")
    @pytest.mark.smoke
    @pytest.mark.basket
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
    @pytest.mark.basket
    def test_add_to_favorite_from_basket(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        cards_list = [page.card.get_product_name()]
        page.card.open_cart()
        page.cart.add_to_favorite()
        page.click_x()
        page.press_back()
        page.open_favorites()
        page.favorites.checking_availability_cards(cards_list)

    @allure.title('Экран "Корзина" / Кнопка "Очистить"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2180")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_delete_all_items(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.cart_clear()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Кнопка очистки корзины (отмена)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1955")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2068")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_close_confirm_of_cleaning(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        cards_name = [page.card.get_product_name()]
        page.card.open_cart()
        page.cart.click_clear_btn()
        page.coordinate_click(100,100)
        page.cart.checking_availability_cards(cards_name)
        page.cart.click_clear_btn()
        page.cart.cancel_confirm_of_cleaning()
        page.cart.checking_availability_cards(cards_name)

    @allure.title('Экран "Корзина" / Кнопка очистки корзины (один товар/очистка)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1954")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_clear_cart_with_one_item(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.cart_clear()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Кнопка очистки корзины (несколько товаров/очистка)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1960")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_clear_cart_with_several_items(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.press_back()
        page.press_back()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.cart_clear()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Кнопка "Очистить" (возврат кдругому экрану корзины)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2578")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_return_to_another_screen(self):
        pass

    @allure.title('Экран "Корзина" / Очистка корзины после успешного оформления')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1980")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_basket_after_order(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.add_main_address()
        page.checkout.set_card_online_selector()
        page.checkout.add_new_card()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.click_x()
        page.open_cart()
        page.cart.check_empty_cart()




