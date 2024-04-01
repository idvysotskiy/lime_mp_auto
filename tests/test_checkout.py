import pytest
from pages.main_page import MainPage
from pages.cart_page import *
from pages.product_card_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestCheckout:
    @allure.title('Экран "Корзина" / Переход к чекауту (Авторизованный)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2869")
    @pytest.mark.smoke
    def test_checkout_with_one_product(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.elements_checkout()


    # @pytest.mark.smoke
    # @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    # @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3048")
    # def test_pay_card(self):
    #     MainPage().login()
    #     page = CheckOutPage()
    #     page.checkout_with_one()
    #     time.sleep(2)
    #     page.checkout_set('1', '2', '1', '1')
    #     time.sleep(2)
    #     page.click_pay()

    # @pytest.mark.smoke
    # @allure.title('Блок "Оплата" / Оплата при получении')
    # @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3038")
    # def test_pay_self(self):
    #     page = CheckOutPage()
    #     page.checkout_with_one()
    #     page.elements_checkout()
    #     page.checkout_set('1', '4', '2', '2')
    #     page.elements_checkout_self()
    #     page.click_pay()
    #     page.continue_shopping()

    @allure.title('Блок "Оплата" / Добавление карты для оплаты')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2946")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2833")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2834")
    @pytest.mark.smoke
    def test_saving_payment_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.add_courier_address()
        page.checkout.add_new_card()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.checking_payment_card_number('4242')

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
        page.checkout.add_courier_address()
        page.checkout.add_new_card()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.checking_payment_card_number('4242')
        page.checkout.deleting_single_payment_card()

    # @pytest.mark.smoke
    # @allure.title('Экран "Оформление заказа" / Не заполнены основные данные')
    # @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/131747")
    # def test_add_main_address_elements(self):
    #     page = CheckOutPage()
    #     page.reg_user()
    #     page.checkout_with_one()
    #     page.click(CheckOutLocators.ADD_ADDRESS_BUTTON)
    #     assert page.get_text(CheckOutLocators.ADD_ADDRESS_TITLE) == 'РЕДАКТИРОВАТЬ АДРЕС'
    #     # ...
    #     assert page.get_text(CheckOutLocators.ADD_ADDRESS_SAVE_BUTTON) == 'СОХРАНИТЬ'
    #     page.get_screen()
    #
    # @pytest.mark.smoke
    # @allure.title('Экран "Оформление заказа" / Заполнение основного адреса ')
    # @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/131748")
    # def test_add_main_address(self):
    #     page = MainPage()
    #     page.reg_kir()
    #     page.click_x()
    #     BasePage().cancel_notification()
    #     page = CheckOutPage()
    #     page.checkout_with_one()
    #     page.add_main_address()
    #     assert page.is_element_present(CheckOutLocators.SELECTED_ADDRESS)
    #     assert page.is_element_present(CheckOutLocators.EDIT_ADDRESS)
    #     page.get_screen()

    @allure.title('Блок "Оплата" / Успешная оплата картой (Нет сохраненных карт)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3147")
    @pytest.mark.smoke
    def test_success_pay_card_with_add_card(self):
        page = MainPage()
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.add_courier_address()
        page.checkout.add_new_card()
        page.swipe_page_up()
        page.checkout.set_date_and_time()
        page.checkout.click_pay()
        page.checkout.click_continue_shopping()

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
        page.swipe_page_up(2)
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
    @pytest.mark.smoke
    @pytest.mark.checkout
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
