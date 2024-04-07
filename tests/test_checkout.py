# file: test_checkout.py
import time

import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
from pages.product_card_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestCheckOut:

    @allure.title('Экран "Корзина" / Переход к чекауту (Авторизованный)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2869")
    @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/136157")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_open_checkout_auth(self, login):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.elements_checkout()
        page.get_screen()
        page.checkout.back_to_cart()

    @allure.title('Экран "Корзина" / Переход к чекауту (Не авторизованный)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2868")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_open_checkout_unauth(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.elements_login_screen()

    @allure.title('Экран "Оформление заказа" / Не заполнены основные данные')
    @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/136163")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2875")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_add_main_address(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.click_add_address_btn()
        page.checkout.elements_add_address()
        page.checkout.add_main_address()
        page.screen_title('ОФОРМЛЕНИЕ ЗАКАЗА')

    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3038")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_pay_self(self):
        page = MainPage()
        # page.clear_basket()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.elements_checkout()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.set_upon_receipt()
        page.checkout.elements_checkout_self()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_upon_receipt()
        # ......
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.elements_checkout()
        page.checkout.set_upon_receipt()
        page.checkout.elements_checkout_self()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_upon_receipt()


    @allure.title('Блок "Оплата" / Сохранение карты')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2946")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2833")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2834")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3181")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_saving_payment_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.checking_payment_card_number('4242')
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Экран "Оформление заказа" / Оплата "Картой онлайн" (Без сохранения карты)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3167")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_payment_card_without_save_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card(save='no')
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.check_btn_add_card()

    @allure.title('Блок "Оплата" / Попап удаления карты')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2948")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2949")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2951")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2952")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2953")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2954")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_delete_last_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.checking_payment_card_number('4242')
        page.checkout.deleting_single_payment_card()

    @allure.title('Блок "Оплата" / Успешная оплата картой (Нет сохраненных карт)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3175")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3188")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3191")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_success_pay_card_with_add_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        # ......
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Экран "Оформление заказа" / Оплата "Картой онлайн"(Не успешно)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3165")
    @allure.testcase("")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_fail_pay_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_fail_cloud_payments()

    @allure.title('Блок "Оплата" / Успешная оплата подарочной картой (Полная стоимость)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3163")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3028")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3032")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_order_courier_gift_card(self, login):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.swipe_page_up()
        page.cart.go_to_checkout()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card(price)
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        # ......
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        page.cart.go_to_checkout()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card(price)
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Блок "Оплата" / Закрытие боттом шита "Добавить подарочную карту" ')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3023")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_closing_gift_card_block(self, login):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.set_gift_card_selector()
        page.checkout.close_gift_card_block()
        page.checkout.set_gift_card_selector()
        page.checkout.close_gift_card_block2()

    @allure.title('Блок "Оплата" / Проверка полей блока Подарочная карта.')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3024")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3025")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3026")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3027")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3029")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_gift_card_fields(self, login):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.set_gift_card_selector()
        page.checkout.checking_gift_card_number(price)
        page.checkout.checking_gift_card_pin_code(price)

    @allure.title('Блок "Оплата" / Доплата картой')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3031")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3035")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_order_with_gift_card_and_additional_payment(self, login):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Блок "Оплата" / Доплата СБП')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3036")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_order_with_gift_card_and_additional_payment_sbp(self, login):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment_sbp()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()

    @allure.title('Экран "Оформление заказа" / Оплата через СБП(Успешное оформление)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2914")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3159")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_order_payment_sbp(self, login):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code(promo_code_2)
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()
        # ......
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()

# -----------------------САМОВЫВОЗ------------------------------------------

    @allure.title('Экран "Оформление заказа" / Оплата "Картой онлайн" (Нет сохраненных карт)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3147")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3161")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_success_pay_card_with_add_card_pickup(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.add_first_card()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        # ......Экран "Оформление заказа" / Успешная оплата "Картой онлайн" (+Промокод)
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.card_online_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Экран "Оформление заказа" / Оплата через СБП(Успешное оформление)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2914")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3159")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_order_payment_sbp(self, login):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code(promo_code_2)
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()
        # ......
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()

    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_pay_self(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.set_upon_receipt()
        page.checkout.elements_checkout_self()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_upon_receipt()
        # ......
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.set_upon_receipt()
        page.checkout.elements_checkout_self()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_upon_receipt()