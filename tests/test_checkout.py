# file: test_checkout.py
import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
from pages.product_card_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestAndroid:
    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Переход к чекауту (Авторизованный)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2869")
    @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/136157")
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

    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Экран "Корзина" / Переход к чекауту (Не авторизованный)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2868")
    def test_open_checkout_unauth(self):
        page = MainPage()
        page.clear_basket()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.elements_login_screen()

    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Экран "Оформление заказа" / Не заполнены основные данные')
    @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/136163")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2875")
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

    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3038")
    def test_pay_self(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.elements_checkout()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.checkout_set('1', '4', '1', '1')
        page.checkout.elements_checkout_self()
        page.swipe_page_up()
        page.checkout.click_pay()
        page.checkout.continue_shopping()

    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Сохранение карты')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2946")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2833")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2834")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3060")
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
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.checking_payment_card_number('4242')
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Попап удаления карты')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2948")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2949")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2951")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2952")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2953")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2954")
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
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.checking_payment_card_number('4242')
        page.checkout.deleting_single_payment_card()
        print("test")

    # @pytest.mark.smoke
    # @allure.title('Экран "Оформление заказа" / Авторизация')
    # @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/131745")
    # def test_go_checkout_unautorized(self):
    #     page = CheckOutPage()
    #     time.sleep(8)
    #     page.checkout_with_one_un()
    #     MainPage().login()
    #     assert page.get_text(MainLocators.TOOLBAR_TITLE) == 'КОРЗИНА'
    #     page.click(MainLocators.PROFILE_NAV)
    #     assert page.is_element_present(ProfileLocators.EMAIL)

    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата картой (Нет сохраненных карт)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3147")
    def test_success_pay_card_with_add_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.add_first_card()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата подарочной картой (Полная стоимость)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3163")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3028")
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
        page.swipe_page_up(1)
        page.checkout.set_date_and_time()
        page.checkout.click_pay()

    @pytest.mark.checkout
    @pytest.mark.smoke
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

    @pytest.mark.checkout
    @pytest.mark.smoke
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

    @pytest.mark.checkout
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Доплата картой')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3031")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3035")
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
        print('test')

