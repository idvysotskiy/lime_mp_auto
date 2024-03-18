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
    @allure.title('Экран "Корзина" / Переход к чекауту (Авторизованный)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2869")
    def test_checkout_with_one_product(self):

        page = CheckOutPage()
        page.checkout_with_one()
        page.back_to_cart()


    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3048")
    def test_pay_card(self):
        MainPage().login()
        page = CheckOutPage()
        page.checkout_with_one()
        time.sleep(2)
        page.checkout_set('1', '2', '1', '1')
        time.sleep(2)
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3038")
    def test_pay_self(self):
        page = CheckOutPage()
        page.checkout_with_one()
        page.elements_checkout()
        page.checkout_set('1', '4', '2', '2')
        page.elements_checkout_self()
        page.click_pay()
        page.continue_shopping()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Сохранение карты')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2946")
    def test_add_new_card(self):
        page = CheckOutPage()
        page.checkout_with_one()
        page.wait_a_second()
        page.click(CheckOut.PAYMENT_SELECTOR_2)
        page.add_new_card()
        page.click(CheckOut.SLOTS_DATE_SELECTOR_1)
        page.click(CheckOut.SLOTS_TIME_SELECTOR_1)
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Попап "Удалить карту (Удалить последнюю карту)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2954")
    def test_delete_last_card(self):
        page = CheckOutPage()
        self.test_add_new_card()
        page.checkout_with_one()
        page.wait_a_second()
        page.click(CheckOut.PAYMENT_SELECTOR_2)
        page.delete_card_solo()
        time.sleep(4)
        BasePage().close_popup()
        page.check_btn_add_card()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Боттом шит "Добавить карту"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2833")
    def test_add_card_elements(self):
        page = CheckOutPage()
        page.reg_user()
        page.checkout_with_one()
        page.click(CheckOut.PAYMENT_SELECTOR_2)
        page.click(CheckOut.ADD_NEW_CARD_PLUS)
        page.elements_add_card()

    @pytest.mark.smoke
    @allure.title('Экран "Оформление заказа" / Не заполнены основные данные')
    @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/131747")
    def test_add_main_address_elements(self):
        page = CheckOutPage()
        page.reg_user()
        page.checkout_with_one()
        page.click(CheckOut.ADD_ADDRESS_BUTTON)
        assert page.get_text(CheckOut.ADD_ADDRESS_TITLE) == 'РЕДАКТИРОВАТЬ АДРЕС'
        # ...
        assert page.get_text(CheckOut.ADD_ADDRESS_SAVE_BUTTON) == 'СОХРАНИТЬ'
        page.get_screen()

    @pytest.mark.smoke
    @allure.title('Экран "Оформление заказа" / Заполнение основного адреса ')
    @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/131748")
    def test_add_main_address(self):
        page = MainPage()
        page.reg_kir()
        page.click_x()
        BasePage().cancel_notification()
        page = CheckOutPage()
        page.checkout_with_one()
        page.add_main_address()
        assert page.is_element_present(CheckOut.SELECTED_ADDRESS)
        assert page.is_element_present(CheckOut.EDIT_ADDRESS)
        page.get_screen()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата картой онлайн (Добавление карты)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2834")
    def test_add_card(self):
        page = MainPage()
        page.reg_kir()
        page.click_x()
        BasePage().cancel_notification()
        page = CheckOutPage()
        page.checkout_with_one()
        page.add_main_address()
        page.click(CheckOut.PAYMENT_SELECTOR_2)
        page.add_new_card()
        assert page.is_element_present(CheckOut.CARD_ICON)
        assert page.is_element_present(CheckOut.CARD_INFO)
        assert page.is_element_present(CheckOut.CARD_EDIT)
        page.get_screen()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата картой (Нет сохраненных карт)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3147")
    def test_success_pay_card_with_add_card(self):
        page = MainPage()
        page.reg_kir()
        page.click_x()
        BasePage().cancel_notification()
        page = CheckOutPage()
        page.checkout_with_one()
        page.add_main_address()
        page.click(CheckOut.PAYMENT_SELECTOR_2)
        page.add_new_card()
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Экран "Оформление заказа" / Авторизация')
    @allure.testcase("https://lmdev.testrail.io/index.php?/tests/view/131745")
    def test_go_checkout_unautorized(self):
        page = CheckOutPage()
        page.checkout_with_one_un()
        MainPage().login()
        assert page.get_text(MainLocators.TOOLBAR_TITLE) == 'КОРЗИНА'
        page.click(MainLocators.PROFILE_NAV)
        assert page.is_element_present(Profile.EMAIL)



