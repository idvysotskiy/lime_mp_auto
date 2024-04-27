# file: test_repeat_payment.py
import time
import pytest
from pages.main_page import MainPage
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Повторная оплата")
class TestRepeatPayments:

    @allure.title('Экран "История заказов" / Кнопка "Назад"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2975")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2965")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2966")
    @pytest.mark.repeat_payment
    @pytest.mark.smoke
    def test_repay_navigation(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.user_registration()
        page.open_catalog()
        page.add_to_cart_random_product()
        page.card.open_cart()
        page.cart.go_to_checkout()
        page.checkout.courier_select()
        page.checkout.click_add_address_btn()
        page.checkout.add_main_address()
        page.checkout.sbp_select()
        page.checkout.set_date_and_time()
        page.repeat.click_pay_sbp_cancel()
        page.repeat.retry_pay_btn()
        page.repeat.orders_navigation_check()





