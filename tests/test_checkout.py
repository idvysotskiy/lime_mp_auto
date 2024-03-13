# file: test_checkout.py
import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
from pages.product_card_page import *
import allure


@pytest.fixture(autouse=True)
def clear_app(d):
    MainPage(d).set_nuxt_02()
    MainPage(d).login(valid_email, valid_password)
    MainPage(d).set_feature_toggles()
    time.sleep(2)
    # MainPage(d).click(MainLocators.CART_NAV)
    # CartPage(d).click(Cart.CLEAR_ALL)
    # CartPage(d).click(Cart.POPUP_CLEAR)
    #
    yield
    d.app_clear(package)


class TestAndroid:
    @allure.title('Экран "Корзина" / Переход к чекауту (Авторизованный)')
    @allure.testcase("C2869")
    def test_checkout_with_one_product(self, d):
        time.sleep(2)
        MainPage(d).click_to_nav_catalog()
        MainPage(d).go_to_catalog_item()
        MainPage(d).go_to_product_card()
        ProductCardPage(d).add_to_cart()
        ProductCardPage(d).select_size(select_size)
        time.sleep(2)
        MainPage(d).go_to_cart()
        # CartPage(d).enter_promo_code(promo_code_2)
        # time.sleep(2)
        CartPage(d).go_to_checkout()
        time.sleep(4)

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("C3048")
    def test_pay_card(self, d):
        page = CheckOutPage(d)
        self.test_checkout_with_one_product(d)
        page.checkout_set('1', '2', '1', '1')
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("C3038")
    def test_pay_self(self, d):
        page = CheckOutPage(d)
        self.test_checkout_with_one_product(d)
        page.elements_checkout()
        page.checkout_set('1', '4', '2', '2')
        page.elements_checkout_self()
        page.click_pay()
        page.continue_shopping()



