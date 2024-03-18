import time
import allure
from pages.base_page import BasePage
from locators import *
from pages.main_page import MainPage
from pages.product_card_page import ProductCardPage
from pages.cart_page import CartPage


class CheckOutPage(BasePage):
    # def __init__(self, d):
    #     super().__init__(d)

    def accept_cloud_payments(self):
        self.d.click(0.504, 0.366)

    @allure.step('Нажать кнопку "Оплатить"')
    def click_pay(self):
        BasePage.swipe_page_up(self)
        time.sleep(0.5)
        self.click(CheckOut.ORDER_PAY)
        time.sleep(5)
        self.accept_cloud_payments()
        time.sleep(1)
        assert self.get_text(SuccessPayScreen.TITLE) == 'ВАШ ЗАКАЗ ПРИНЯТ'
        assert self.get_text(SuccessPayScreen.DESCRIPTION) == 'Отслеживать его статус вы можете в личном кабинете'
        assert self.get_text(SuccessPayScreen.BUTTON) == 'ПРОДОЛЖИТЬ ПОКУПКИ'
        BasePage.get_screen(self)

    def checkout_set(self, delivery_method, pay_method, date_slot, time_slot):
        with allure.step("Выбрать способ доставки '{delivery_method}'"):
            if delivery_method == '1':
                self.click(CheckOut.DELIVERY_SELECTOR_1)
            elif delivery_method == '2':
                self.click(CheckOut.DELIVERY_SELECTOR_2)
            elif delivery_method == '3':
                self.click(CheckOut.DELIVERY_SELECTOR_3)
            time.sleep(1)
        with allure.step("Выбрать способ оплаты '{pay_method}'"):
            if pay_method == '1':
                self.click(CheckOut.PAYMENT_SELECTOR_1)
            elif pay_method == '2':
                self.click(CheckOut.PAYMENT_SELECTOR_2)
            elif pay_method == '3':
                self.click(CheckOut.PAYMENT_SELECTOR_3)
            elif pay_method == '4':
                self.click(CheckOut.PAYMENT_SELECTOR_4)
            time.sleep(1)
        with allure.step("Выбрать дату доставки '{date_slot}'"):
            if date_slot == '1':
                self.click(CheckOut.SLOTS_DATE_SELECTOR_1)
            elif date_slot == '2':
                self.click(CheckOut.SLOTS_DATE_SELECTOR_2)
            elif date_slot == '3':
                self.click(CheckOut.SLOTS_DATE_SELECTOR_3)
            time.sleep(1)
        with allure.step("Выбрать время доставки '{time_slot}'"):
            if time_slot == '1':
                self.click(CheckOut.SLOTS_TIME_SELECTOR_1)
            elif time_slot == '2':
                self.click(CheckOut.SLOTS_TIME_SELECTOR_2)
            elif time_slot == '3':
                self.click(CheckOut.SLOTS_TIME_SELECTOR_3)
        BasePage.get_screen(self)

    def elements_checkout(self):
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'ОФОРМЛЕНИЕ ЗАКАЗА'
        assert self.get_text(CheckOut.DELIVERY_TITLE) == 'ВЫБЕРИТЕ СПОСОБ ДОСТАВКИ'
        assert self.get_text(CheckOut.PAYMENT_TITLE) == 'ВЫБЕРИТЕ СПОСОБ ОПЛАТЫ'
        assert self.get_text(CheckOut.ORDER_LIST_TITLE) == 'СОСТАВ ЗАКАЗА'

    def elements_checkout_self(self):
        assert self.get_text(CheckOut.PAYMENT_TITLE_4) == 'ПРИ ПОЛУЧЕНИИ'
        assert self.get_text(CheckOut.PAYMENT_INFO_TEXT) == 'Наличными или картой при получении'

    @allure.title('Блок "Оплата" / Успешная оплата (Кнопка продолжить покупки)')
    @allure.testcase("C3050")
    def continue_shopping(self):
        self.click(SuccessPayScreen.BUTTON)
        time.sleep(2)
        assert self.get_text(Catalog.WOMEN) == 'ЖЕНЩИНЫ'
        assert self.get_text(Catalog.MEN) == 'МУЖЧИНЫ'
        assert self.get_text(Catalog.KIDS) == 'ДЕТИ'
        self.is_element_present(MainLocators.X_BUTTON)
        BasePage.get_screen(self)

    def back_to_cart(self):
        self.click(MainLocators.X_BUTTON)
        self.click(CheckOut.POPUP_BACK_CART_YES)

    def checkout_with_one(self):
        ProductCardPage().add_one_product_to_cart()
        CartPage().go_to_checkout()
        time.sleep(2)
        self.elements_checkout()
        BasePage().get_screen()

    def checkout_with_one_un(self):
        ProductCardPage().add_one_product_to_cart()
        CartPage().go_to_checkout()
        self.get_screen()

    def delete_card_solo(self):
        with allure.step('Нажать на иконку "Карандаш" справа от данных карты'):
            self.click(CheckOut.CARD_EDIT)
        with allure.step('Нажать иконку "Корзина" справа от данных карты'):
            self.click(CheckOut.CARD_DELETE_SOLO)
        with allure.step('Нажать кнопку "Удалить"'):
            self.click(CheckOut.DEL_CARD_POP_UP_DELETE)
        with allure.step('Закрыть боттом шит "Ваши карты"'):
            self.click(MainLocators.X_BUTTON)

    def add_new_card(self):
        with allure.step('Нажать кнопку "Добавить карту"'):
            self.click(CheckOut.ADD_NEW_CARD_PLUS)
            self.wait_element(CheckOut.ADD_CARD_TITLE)
            assert self.get_text(CheckOut.ADD_CARD_TITLE) == 'ДОБАВИТЬ КАРТУ'
        with allure.step('Заполнить поля валидными данными'):
            self.set_text(CheckOut.ADD_CARD_NUMBER, card_1)
            self.set_text(CheckOut.ADD_CARD_OWNER, card_owner)
            self.set_text(CheckOut.ADD_CARD_EXPIRY, card_expiry)
            self.set_text(CheckOut.ADD_CARD_CVV, card_cvv)
        # with allure.step('Выбрать чекбокс "Запомнить данные карты'):
        #     self.click(CheckOut.ADD_CARD_SAVE_CHECK_BOX)
            self.get_screen()
        with allure.step('Нажать кнопку "Сохранить"'):
            self.click(CheckOut.ADD_CARD_SAVE_BUTTON)
        self.get_screen()

    def check_btn_add_card(self):
        self.is_element_present(CheckOut.ADD_NEW_CARD_PLUS)

    def add_main_address(self):
        with allure.step('Нажать кнопку "Добавить адрес"'):
            self.click(CheckOut.ADD_ADDRESS_BUTTON)
        with allure.step('Ввести значение в поле "Город"'):
            self.set_text(CheckOut.ADD_ADDRESS_CITY, 'Новосибирск')
        with allure.step('Выбрать город из всплывашки'):
            self.click(CheckOut.ADD_ADDRESS_POPUP)
        with allure.step('Ввести значение в поле "Улица"'):
            self.set_text(CheckOut.ADD_ADDRESS_STREET, 'Лаврентьева 6/1')
        with allure.step('Выбрать улицу из всплывашки'):
            self.click(CheckOut.ADD_ADDRESS_POPUP)
        with allure.step('Ввести значение в поле "Квартира"'):
            self.set_text(CheckOut.ADD_ADDRESS_APARTMENT, '605')
        self.get_screen()
        with allure.step('Нажать кнопку "Сохранить"'):
            self.click(CheckOut.ADD_ADDRESS_SAVE_BUTTON)

    def elements_add_card(self):
        assert self.get_text(CheckOut.ADD_CARD_TITLE) == 'ДОБАВИТЬ КАРТУ'
        assert self.get_text(CheckOut.ADD_CARD_NUMBER) == 'Номер карты'
        assert self.get_text(CheckOut.ADD_CARD_OWNER) == 'Владелец карты'
        assert self.get_text(CheckOut.ADD_CARD_EXPIRY) == 'Месяц / год'
        assert self.get_text(CheckOut.ADD_CARD_CVV) == 'CVV / CVC'
        assert self.get_text(CheckOut.ADD_CARD_SAVE_CHECK_BOX) == 'Запомнить данные карты'
        assert self.get_text(CheckOut.ADD_CARD_SAVE_BUTTON) == 'СОХРАНИТЬ'
        self.get_screen()

    def reg_user(self):
        page = MainPage()
        page.reg_kir()
        page.click_x()
        self.cancel_notification()
