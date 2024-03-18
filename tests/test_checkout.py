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
        CheckOutPage().checkout_with_one()
        CheckOutPage().back_to_cart()
        time.sleep(2)
        CartPage().cart_clear()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3048")
    def test_pay_card(self):
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
        page.checkout_with_one()
        page.click(CheckOut.PAYMENT_SELECTOR_2)
        page.delete_card_solo()
        time.sleep(4)
        BasePage().close_popup()
        page.check_btn_add_card()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата картой онлайн (Нет сохраненных карт)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2833")
    def test_full_buy(self):
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



