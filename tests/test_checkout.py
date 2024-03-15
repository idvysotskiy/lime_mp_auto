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
        time.sleep(2)
        main = MainPage()
        product_card_page = ProductCardPage()
        main.click_to_nav_catalog()
        main.go_to_catalog_item()
        main.go_to_product_card()
        product_card_page.add_to_cart()
        product_card_page.select_size(select_size)
        time.sleep(2)
        main.go_to_cart()
        # CartPage(d).enter_promo_code(promo_code_2)
        # time.sleep(2)
        CartPage().go_to_checkout()
        time.sleep(4)

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("C3048")
    def test_pay_card(self, login):
        page = CheckOutPage()
        self.test_checkout_with_one_product()
        page.checkout_set('1', '2', '1', '1')
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("C3038")
    def test_pay_self(self):
        page = CheckOutPage()
        self.test_checkout_with_one_product()
        page.elements_checkout()
        page.checkout_set('1', '4', '2', '2')
        page.elements_checkout_self()
        page.click_pay()
        page.continue_shopping()



