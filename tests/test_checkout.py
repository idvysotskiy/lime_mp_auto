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
    @allure.testcase("C2869")
    def test_checkout_with_one_product(self):
        CheckOutPage().checkout_with_one()
        CheckOutPage().back_to_cart()
        time.sleep(2)
        CartPage().cart_clear()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("C3048")
    def test_pay_card(self):
        page = CheckOutPage()
        page.checkout_with_one()
        time.sleep(2)
        page.checkout_set('1', '2', '1', '1')
        time.sleep(2)
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("C3038")
    def test_pay_self(self):
        page = CheckOutPage()
        page.checkout_with_one()
        page.elements_checkout()
        page.checkout_set('1', '4', '2', '2')
        page.elements_checkout_self()
        page.click_pay()
        page.continue_shopping()



