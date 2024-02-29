# file: test_checkout.py
import pytest
from pages.main_page import MainPage
from pages.checkout_page import CheckOutPage
from pages.base_page import *
from pages.cart_page import *
from pages.product_card_page import *
import allure


# @pytest.fixture(autouse=True)
# def clear_app(device):
#     MainPage(device).set_nuxt_02()
#     MainPage(device).login(valid_email, valid_password)
#     page.set_feature_toggles()
#     time.sleep(2)
#     MainPage(device).click(MainLocators.X_BUTTON)
#     yield
#     device.app_clear(package)


class TestAndroid:
    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Успешная оплата ранее сохраненной картой')
    @allure.testcase("C3048")
    def test_pay_card(self, device):
        page = CheckOutPage(device)
        page.checkout_with_one_product()
        page.checkout_set('1', '2', '1', '1')
        page.click_pay()

    @pytest.mark.smoke
    @allure.title('Блок "Оплата" / Оплата при получении')
    @allure.testcase("C3038")
    def test_pay_self(self, device):
        page = CheckOutPage(device)
        page.checkout_with_one_product()
        page.elements_checkout()
        page.checkout_set('1', '4', '2', '2')
        page.elements_checkout_self()
        page.click_pay()
        page.continue_shopping()



