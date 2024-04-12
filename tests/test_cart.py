from pages.main_page import MainPage
from pages.cart_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Корзина")
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
        # page.open_profile()
        # page.swipe_page_up(2)
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
        # page.open_profile()
        # page.swipe_page_up(2)
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
        # page.open_profile()
        # page.swipe_page_up(2)
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
        page.coordinate_click(100, 100)
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

    @allure.title('Экран "Корзина" / Кнопка "Очистить" (возврат к другому экрану корзины)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2578")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_return_to_another_screen(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        card_size = page.cart.get_size()
        page.cart.open_card()
        page.card.add_to_cart_more_item(card_size)
        page.card.open_cart()
        page.cart.cart_clear()
        page.click_x()
        page.click(ProductCardLocators.back_btn, "кнопка Назад")
        page.cart.check_empty_cart()

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
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.card_online_select()
        page.checkout.add_first_card()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.accept_cloud_payments()
        page.checkout.click_continue_shopping()
        page.click_x()
        page.open_cart()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Поле "Промокод" (ввод валидного значения). Очистка поля Промокод')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2038")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2040")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_promo_valid_value_and_clear_promo_field(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.set_valid_promo()
        page.cart.clear_promo_field()

    @allure.title('Экран "Корзина" / Поле "Промокод" (ввод валидного значения после невалидного)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2618")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2039")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_promo_valid_after_invalid_value(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.set_invalid_promo()
        page.cart.set_valid_promo()

    @allure.title('Экран "Корзина" / Отображение поля "Промокод" после авторизации/регистрации')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2025")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2871")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_promo_after_authorization(self):
        page = MainPage()
        email = page.user_registration()
        # page.open_profile()
        # page.swipe_page_up(2)
        page.profile.logout()
        page.click_x()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.set_valid_promo()
        page.cart.go_to_checkout()
        page.cart.authorization(email)
        page.cart.check_valid_promo_message()

    @allure.title('Экран "Корзина" / Сброс промокода при закрытии экрана (Не авторизован)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2700")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_reset_promo_after_close_basket_without_authorization(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.set_valid_promo()
        page.click_x()
        page.card.open_cart()
        page.cart.check_clear_promo()

    @allure.title('Экран "Корзина" / Сброс промокода при закрытии экрана (Авторизован)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2017")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_reset_promo_after_close_basket_with_authorization(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.set_valid_promo()
        page.click_x()
        page.card.open_cart()
        page.cart.check_clear_promo()

    @allure.title('Экран "Корзина" / Удаление последнего товара из корзины при введенном промокоде')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2215")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_delete_item_with_promo(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.set_valid_promo()
        page.cart.delete_item()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Очистка корзины при введенном промокоде')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2214")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_clear_cart_with_promo(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.set_valid_promo()
        page.cart.cart_clear()
        page.cart.check_empty_cart()

    @allure.title('Экран "Корзина" / Сохранение скидки при переходе к экрану "Оформление заказа"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2041")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_save_promo_after_go_to_checkout(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.set_valid_promo()
        page.wait_a_second()
        price_in_cart = page.cart.get_price_sale()
        page.cart.go_to_checkout()
        page.swipe_page_up()
        page.wait_a_second()
        price_in_checkout = page.checkout.get_summary_total()
        assert price_in_cart == price_in_checkout, print(
            f"Сумма в корзине и чекауте отличаются. Сумма в корзине: {price_in_cart}, сумма в чекауте: {price_in_checkout}")

    @allure.title('Экран "Корзина" / Регистрация')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2872")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_registration_in_cart(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        card_name = page.card.get_product_name()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.cart.registration()
        assert card_name == page.get_text(CartLocators.PRODUCT_TITLE), print(
            f"Название товара в корзине после регистрации изменилось. До регистрации {card_name}, после регистрации {page.get_text(CartLocators.PRODUCT_TITLE)}")

    @allure.title('Экран "Корзина" / Отображение поля Промокод при удалении одного из товаров')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2026")
    @pytest.mark.smoke
    @pytest.mark.basket
    def test_check_promo_after_delete_one_item(self):
        page = MainPage()
        page.open_catalog()
        page.add_to_cart_random_product()
        total_price = page.card.get_product_price()
        page.press_back()
        page.press_back()
        page.add_to_cart_random_product()
        total_price += page.card.get_product_price()
        page.card.open_cart()
        page.swipe_page_up()
        page.cart.set_valid_promo()
        assert int(total_price * 0.9) == page.get_number_from_element(CartLocators.FINAL_PRICE), print(
            f"Скидка не активна. Сумма товаров со скидкой = {int(total_price * 0.9)}, сумма Итого = {page.get_number_from_element(CartLocators.FINAL_PRICE)}")
        page.cart.delete_item()
        page.cart.check_valid_promo_message()
        assert int(page.get_number_from_element(CartLocators.SUMMARY_PRICE) * 0.9) == page.get_number_from_element(
            CartLocators.FINAL_PRICE), print(
            f"Скидка не активна после удаления одного из двух товаров. Сумма товаров = {int(page.get_number_from_element(CartLocators.SUMMARY_PRICE) * 0.9)}, сумма Итого = {page.get_number_from_element(CartLocators.FINAL_PRICE)}")

    @allure.title('Экран "Корзина" / Поле "Промокод" (Учет скидки в стоимости)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3356")
    @pytest.mark.basket
    @pytest.mark.smoke
    def test_promo_code_discount(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.enter_promo_code()
        discount = page.cart.get_cart_discount()
        price_with_discount = page.cart.get_cart_price()
        assert price - discount == price_with_discount, f'Итоговая цена {price_with_discount} не равна разности исходной цены {price} и скидке {discount}'

