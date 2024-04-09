# file: test_checkout.py
import time
import pytest
from pages.main_page import MainPage
from pages.cart_page import *
from pages.product_card_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Оформление заказа")
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

    @allure.title('Блок "Оформление заказа" / Кнопка "Оплатить" (Снек-бар)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3312")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2955")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2765")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_checkout_error(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.click_pay_check_warnings()

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
        page.checkout.courier_select()
        page.checkout.click_add_address_btn()
        page.checkout.elements_add_address()
        page.checkout.add_main_address()
        page.screen_title('ОФОРМЛЕНИЕ ЗАКАЗА')

    @allure.title('Блок "Оплата" / Курьером / Оплата при получении')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3189")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3172")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_pay_self(self):
        page = MainPage()
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
        page.checkout.elements_success_pay()

        # ......Блок "Оплата" / Оплата при получении +Промокод
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
        page.checkout.elements_success_pay()

    @allure.title('Блок "Оплата" / Курьером / Сохранение карты')
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
        page.checkout.courier_select()
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

    @allure.title('Экран "Оформление заказа" / Курьером / Успешный результат без 3-D Secure')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3183")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_payment_card_without_3ds(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card(card_8)
        page.checkout.set_date_and_time()
        page.checkout.click_pay_without_3ds()
        page.checkout.elements_success_pay()

    @allure.title('Экран "Оформление заказа" / Курьером / Недостаточно средств на карте без 3-D Secure')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3185")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_no_funds_payment_card_without_3ds(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card(card_15)
        page.wait_a_moment()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_without_3ds()
        page.checkout.elements_pay_no_funds()

    @allure.title('Экран "Оформление заказа" / Курьером / Недостаточно средств на карте 3-D Secure')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3184")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_no_funds_payment_card_with_3ds(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card(card_15)
        page.wait_a_moment()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_no_funds()
        page.checkout.elements_pay_no_funds()

    @allure.title('Блок "Состав заказа" / Учет скидки по промокоду')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3344")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2810")
    @pytest.mark.checkout
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
        # assert price - discount == price_with_discount, f'Итоговая цена {price_with_discount} не равна разности исходной цены {price} и скидке {discount}'
        page.cart.go_to_checkout()
        page.swipe_page_up()
        page.checkout.open_order_list()
        page.swipe_page_up()
        price_order_list = page.checkout.get_order_list_price_with_discount()
        assert price_order_list == price_with_discount, f'Итоговая цена из корзины{price_with_discount} не совпадает с ценой в составе заказа {price_order_list}'
        summary_discount = page.checkout.get_summary_discount()
        assert discount == summary_discount, f"Скидка с экрана Корзина {discount} не совпадает со скидкой на экране Оформление заказа {summary_discount}"
        summary_coast = page.checkout.get_summary_coast()
        summary_total = page.checkout.get_summary_total()
        assert price == summary_coast, f'Стоимость с карточки товара {price} не совпадает с стоимостью в блоке саммери {summary_coast}'
        assert price_with_discount == summary_total, f'Стоимость товара со скидкой {price_with_discount} с экрана корзина не совпадает с стоимостью со скидкой в блоке саммери {summary_total}'

    @allure.title('Экран "Оформление заказа" / Курьером / Оплата "Картой онлайн" (Без сохранения карты)')
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
        page.checkout.courier_select()
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
        page.checkout.courier_select()
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

    @allure.title('Блок "Оплата" / Курьером / Успешная оплата картой (Нет сохраненных карт)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3175")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3188")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3174")
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
#         # ...... Успешная оплата картой +Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
#

    @allure.title('Экран "Оформление заказа" / Курьером / Оплата "Картой онлайн"(Не успешно)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3193")
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

    @allure.title('Блок "Оплата" / Курьером / Успешная оплата подарочной картой (Полная стоимость)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3163")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3028")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3187")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3169")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_order_courier_gift_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.swipe_page_up()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card(price)
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        # ...... Успешная оплата подарочной картой (Полная стоимость) + Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        price = page.cart.get_cart_price()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card(price)
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Блок "Оплата" / Закрытие боттом шита "Добавить подарочную карту" ')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3023")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_closing_gift_card_block(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
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
    def test_gift_card_fields(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.set_gift_card_selector()
        page.checkout.checking_gift_card_number(price)
        page.checkout.checking_gift_card_pin_code(price)

    @allure.title('Экран "Оформление заказа" / Курьером / Оплата через СБП(Успешное оформление)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3166")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3190")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_order_payment_sbp(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()
        # ...... Оплата через СБП + Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code(promo_code_2)
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()

    @allure.title('Блок "Оплата" / Курьером / Доплата картой')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3031")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3035")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3171")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3314")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_order_with_gift_card_and_additional_payment(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        # ......Доплата картой +Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        price = page.cart.get_cart_price()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Блок "Оплата" / Курьером / Доплата СБП')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3170")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3315")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_order_with_gift_card_and_additional_payment_sbp(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment_sbp()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()
        # ......Доплата СБП +Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        price = page.cart.get_cart_price()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment_sbp()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()

# -----------------------САМОВЫВОЗ------------------------------------------

    @allure.title('Экран "Оформление заказа" / Самовывоз / Оплата "Картой онлайн" (Нет сохраненных карт)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3147")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3050")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3161")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_pickup_success_pay_card_with_add_card(self):
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

    @allure.title('Экран "Оформление заказа" / Самовывоз / Оплата через СБП(Успешное оформление)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2914")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3159")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_pickup_order_payment_sbp(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()
        # ...... Оплата через СБП(Успешное оформление) + Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code(promo_code_2)
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()

    @allure.title('Блок "Оплата" / Самовывоз / Успешная оплата подарочной картой (Полная стоимость)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3112")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3032")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_pickup_order_courier_gift_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.swipe_page_up()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card(price)
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        # ...... Успешная оплата подарочной картой (Полная стоимость) + Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        price = page.cart.get_cart_price()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card(price)
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Блок "Оплата" / Самовывоз / Оплата при получении')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3150")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3038")
    @allure.testcase("")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_pickup_pay_self(self):
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
        page.checkout.elements_success_pay()
        # ...... 'Блок "Оплата" / Оплата при получении' + Промокод
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
        page.checkout.elements_success_pay()

    @allure.title('Блок "Оплата" / Самовывоз / Доплата картой')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3037")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3317")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_pickup_order_with_gift_card_and_additional_payment(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        # ......Доплата картой +Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        price = page.cart.get_cart_price()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Блок "Оплата" / Самовывоз / Доплата СБП')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3036")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3316")
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_pickup_order_with_gift_card_and_additional_payment_sbp(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        price = page.card.get_product_price()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment_sbp()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()
        # ...... Доплата СБП +Промокод
        page.checkout.continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.enter_promo_code()
        price = page.cart.get_cart_price()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.set_gift_card_selector()
        page.checkout.set_gift_card_with_additional_payment(price)
        page.checkout.add_additional_payment_sbp()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_sbp()

    @allure.title('Экран "Оформление заказа" / Самовывоз / Оплата "Картой онлайн" (Без сохранения карты)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3015")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_pickup_payment_card_without_save_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.add_first_card(save='no')
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.check_btn_add_card()

    @allure.title('Блок "Оплата" / Самовывоз / Сохранение карты')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3066")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3060")
    @pytest.mark.checkout
    @pytest.mark.smoke
    def test_pickup_saving_payment_card(self):
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
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.pickup_select_pvz()
        page.checkout.checking_payment_card_number('4242')
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @allure.title('Экран "Оформление заказа" / Самовывоз / Оплата "Картой онлайн"(Не успешно)')
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
        page.checkout.pickup_select_pvz()
        page.checkout.add_first_card()
        page.checkout.set_date_and_time()
        page.checkout.click_pay_fail_cloud_payments()



