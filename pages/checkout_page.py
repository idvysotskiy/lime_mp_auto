import time
import allure
from pages.base_page import BasePage
from locators import *


class CheckOutPage(BasePage):

    @allure.step('Нажать кнопку "Успешно" на экране Cloud Payments')
    def accept_cloud_payments(self):
        # self.wait_element(CheckOutLocators.cloud_payments)
        time.sleep(2)
        self.get_screen()
        self.d.click(0.504, 0.360)
        self.wait_a_moment()
        self.d.click(0.504, 0.470)
        time.sleep(2)

    @allure.step('Нажать кнопку "Неудача" на экране Cloud Payments')
    def fail_cloud_payments(self):
        # self.wait_element(CheckOutLocators.cloud_payments)
        time.sleep(2)
        self.get_screen()
        self.d.click(0.504, 0.450)
        time.sleep(2)
        self.d.click(0.504, 0.560)

    @allure.step('Нажать кнопку "Оплатить"')
    def click_pay(self):
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)

    def elements_success_pay(self):
        self.wait_element(SuccessPayScreenLocators.TITLE)
        assert self.get_text(SuccessPayScreenLocators.TITLE) == 'ВАШ ЗАКАЗ ПРИНЯТ'
        assert self.get_text(
            SuccessPayScreenLocators.DESCRIPTION) == 'Отслеживать его статус вы можете в личном кабинете'
        assert self.get_text(SuccessPayScreenLocators.BUTTON) == 'ПРОДОЛЖИТЬ ПОКУПКИ'
        self.get_screen()

    def click_pay_no_funds(self):
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)
        time.sleep(5)
        self.accept_cloud_payments()
        time.sleep(1)
        self.wait_element(SuccessPayScreenLocators.TITLE)

    @allure.step('Нажать кнопку "Оплатить"')
    def click_pay_without_3ds(self):
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)
        self.wait_element(SuccessPayScreenLocators.TITLE)

    def elements_success_pay(self):
        assert self.get_text(SuccessPayScreenLocators.TITLE) == 'ВАШ ЗАКАЗ ПРИНЯТ'
        assert self.get_text(
            SuccessPayScreenLocators.DESCRIPTION) == 'Отслеживать его статус вы можете в личном кабинете'
        assert self.get_text(SuccessPayScreenLocators.BUTTON) == 'ПРОДОЛЖИТЬ ПОКУПКИ'
        self.get_screen()

    def elements_pay_no_funds(self):
        assert self.get_text(SuccessPayScreenLocators.TITLE) == 'ОПЛАТА НЕ ПРОШЛА'
        self.wait_text('Мы сохранили ваш заказ в личном кабинете — оплатите его в течение')
        assert self.get_text(SuccessPayScreenLocators.BUTTON) == 'ПОВТОРИТЬ ПОПЫТКУ'
        self.get_screen()

    @allure.step('Нажать кнопку "Оплатить"')
    def click_pay_check_warnings(self):
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)
        # self.wait_element(MainLocators.snack_bar_message)
        assert self.get_text(MainLocators.snack_bar_message) == 'Не выбран адрес доставки'
        self.click(CheckOutLocators.ADD_ADDRESS_BUTTON)
        self.add_main_address()
        self.wait_a_second()
        self.click(CheckOutLocators.card_online_selector)
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)
        # self.wait_element(MainLocators.snack_bar_message)
        assert self.get_text(MainLocators.snack_bar_message) == 'Не выбрана карта для оплаты'
        self.add_first_card()
        self.click(CheckOutLocators.ORDER_PAY)
        # self.wait_element(MainLocators.snack_bar_message)
        assert self.get_text(MainLocators.snack_bar_message) == 'Не выбрана дата или время доставки'
        self.set_date_and_time()

    @allure.step('Нажать кнопку "Заказать"')
    def click_pay_upon_receipt(self):
        self.wait_a_second()
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)

    @allure.step('Нажать кнопку "Оплатить"')
    def click_pay_fail_cloud_payments(self):
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)
        time.sleep(5)
        self.fail_cloud_payments()
        time.sleep(5)
        self.wait_element(SuccessPayScreenLocators.TITLE)
        assert self.get_text(SuccessPayScreenLocators.TITLE) == 'ОПЛАТА НЕ ПРОШЛА'
        assert self.get_text(
            SuccessPayScreenLocators.DESCRIPTION_FAIL) == 'Мы сохранили ваш заказ в личном кабинете — оплатите его в течение 8 минут'
        assert self.get_text(SuccessPayScreenLocators.BUTTON) == 'ПОВТОРИТЬ ПОПЫТКУ'
        self.get_screen()

    @allure.step('Нажать кнопку "Оплатить" (СБП)')
    def click_pay_sbp(self):
        self.wait_a_second()
        self.swipe_page_up()
        self.wait_a_second()
        self.click(CheckOutLocators.ORDER_PAY)
        self.wait_element(CheckOutLocators.SBP_BANK_LIST_TITLE)
        self.get_screen()
        self.click(CheckOutLocators.SBP_SELECTOR_TINKOFF)
        time.sleep(5)
        self.accept_cloud_payments()
        self.press_back()
        # self.wait_element(CheckOutLocators.STATUS_PAY_TITLE)
        time.sleep(5)
        assert self.get_text(CheckOutLocators.STATUS_PAY_TITLE) == 'ОЖИДАЕМ ПОДТВЕРЖДЕНИЕ ПЛАТЕЖА'
        self.get_screen()
        time.sleep(100)
        assert self.get_text(CheckOutLocators.STATUS_PAY_TITLE) == 'ВАШ ЗАКАЗ ПРИНЯТ'
        self.get_screen()

    # @allure.step('Выбрать элементы на экране Оформление заказа')
    # def checkout_set(self, delivery_method, pay_method, date_slot, time_slot):
    #     with allure.step(f"Выбрать способ доставки '{delivery_method}'"):
    #         if delivery_method == '1':
    #             self.click(CheckOutLocators.DELIVERY_SELECTOR_1)
    #         elif delivery_method == '2':
    #             self.click(CheckOutLocators.DELIVERY_SELECTOR_2)
    #         elif delivery_method == '3':
    #             self.click(CheckOutLocators.DELIVERY_SELECTOR_3)
    #         time.sleep(1)
    #     with allure.step(f"Выбрать способ оплаты '{pay_method}'"):
    #         if pay_method == '1':
    #             self.click(CheckOutLocators.PAYMENT_SELECTOR_1)
    #         elif pay_method == '2':
    #             self.click(CheckOutLocators.PAYMENT_SELECTOR_2)
    #         elif pay_method == '3':
    #             self.click(CheckOutLocators.PAYMENT_SELECTOR_3)
    #         elif pay_method == '4':
    #             self.click(CheckOutLocators.PAYMENT_SELECTOR_4)
    #         time.sleep(1)
    #     with allure.step(f"Выбрать дату доставки '{date_slot}'"):
    #         if date_slot == '1':
    #             self.click(CheckOutLocators.SLOTS_DATE_SELECTOR_1)
    #         elif date_slot == '2':
    #             self.click(CheckOutLocators.SLOTS_DATE_SELECTOR_2)
    #         elif date_slot == '3':
    #             self.click(CheckOutLocators.SLOTS_DATE_SELECTOR_3)
    #         time.sleep(1)
    #     with allure.step(f"Выбрать время доставки '{time_slot}'"):
    #         if time_slot == '1':
    #             self.click(CheckOutLocators.SLOTS_TIME_SELECTOR_1)
    #         elif time_slot == '2':
    #             self.click(CheckOutLocators.SLOTS_TIME_SELECTOR_2)
    #         elif time_slot == '3':
    #             self.click(CheckOutLocators.SLOTS_TIME_SELECTOR_3)
    #     self.get_screen()

    @allure.step('Проверить элементы на экране Оформление заказа')
    def elements_checkout(self):
        self.wait_text("ОФОРМЛЕНИЕ ЗАКАЗА")
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'ОФОРМЛЕНИЕ ЗАКАЗА'
        assert self.get_text(CheckOutLocators.DELIVERY_TITLE) == 'ВЫБЕРИТЕ СПОСОБ ДОСТАВКИ'
        assert self.get_text(CheckOutLocators.PAYMENT_TITLE) == 'ВЫБЕРИТЕ СПОСОБ ОПЛАТЫ'
        # assert self.get_text(CheckOutLocators.ORDER_LIST_TITLE) == 'СОСТАВ ЗАКАЗА'
        self.get_screen()

    def elements_checkout_self(self):
        # assert self.get_text(CheckOutLocators.PAYMENT_TITLE_4) == 'ПРИ ПОЛУЧЕНИИ'
        assert self.get_text(CheckOutLocators.PAYMENT_INFO_TEXT) == 'Наличными или картой при получении'
        self.get_screen()

    @allure.step('Нажать кнопку "Продолжить покупки"')
    def continue_shopping(self):
        self.click(SuccessPayScreenLocators.BUTTON)
        time.sleep(2)
        assert self.get_text(CatalogLocators.WOMEN) == 'ЖЕНЩИНЫ'
        assert self.get_text(CatalogLocators.MEN) == 'МУЖЧИНЫ'
        assert self.get_text(CatalogLocators.KIDS) == 'ДЕТИ'
        self.is_element_present(MainLocators.X_BUTTON)
        self.get_screen()

    @allure.step('Вернуться в корзину с экрана Оформление заказа')
    def back_to_cart(self):
        self.click(MainLocators.X_BUTTON)
        self.wait_element(CheckOutLocators.POPUP_BACK_CART_TITLE)
        self.get_screen()
        assert self.get_text(CheckOutLocators.POPUP_BACK_CART_TITLE) == 'Хотите вернуться в корзину?'
        assert self.get_text(
            CheckOutLocators.POPUP_BACK_CART_DESCRIPTION) == 'При возвращении в корзину все заполненные данные будут сброшены'
        assert self.get_text(CheckOutLocators.POPUP_BACK_CART_CANCEL) == 'ОТМЕНА'
        # assert self.get_text(CheckOutLocators.POPUP_BACK_CART_YES) == 'Вернуться в корзину'
        self.get_screen()
        self.click(CheckOutLocators.POPUP_BACK_CART_YES)
        assert self.get_text(MainLocators.TOOLBAR_TITLE) == 'КОРЗИНА'
        self.get_screen()

    @allure.step("Удаление единственной карты")
    def deleting_single_payment_card(self):
        self.click(CheckOutLocators.CARD_EDIT, "иконка редактирования карты")
        self.wait_text("ВАШИ КАРТЫ")
        self.press_back()
        self.checking_payment_card_number('4242')
        self.click(CheckOutLocators.CARD_EDIT, "иконка редактирования карты")
        self.click(CheckOutLocators.CARD_DELETE_SOLO, "иконка удаления карты")
        self.coordinate_click(100, 100)
        self.checking_card_list('4242')
        self.click(CheckOutLocators.CARD_DELETE_SOLO, "иконка удаления карты")
        self.get_screen()
        self.click(CheckOutLocators.POPUP_BACK_CART_YES, "кнопка Отмена")
        self.checking_card_list('4242')
        self.click(CheckOutLocators.CARD_DELETE_SOLO, "иконка удаления карты")
        self.click(CheckOutLocators.DEL_CARD_POP_UP_DELETE, "кнопка Удалить")
        self.wait_element(CheckOutLocators.ADD_NEW_CARD_BUTTON, "кнопка Добавить карту на модальном окне Ваши карты")
        self.press_back()
        self.wait_element(CheckOutLocators.ADD_NEW_CARD_PLUS, "кнопка Добавить карту + на экране Оформление заказа")
        self.get_screen()

    @allure.step("Добавление новой карты для оплаты заказ")
    def add_first_card(self, card_number=card_1, save='yes'):
        self.card_online_select()
        self.wait_element(CheckOutLocators.ADD_NEW_CARD_PLUS)
        with allure.step('Нажать кнопку "Добавить карту"'):
            self.click(CheckOutLocators.ADD_NEW_CARD_PLUS)
            self.wait_element(CheckOutLocators.ADD_CARD_TITLE)
            assert self.get_text(CheckOutLocators.ADD_CARD_TITLE) == 'ДОБАВИТЬ КАРТУ'
        with allure.step('Заполнить поля валидными данными'):
            self.set_text(CheckOutLocators.ADD_CARD_NUMBER, card_number)
            self.set_text(CheckOutLocators.ADD_CARD_OWNER, card_owner)
            self.set_text(CheckOutLocators.ADD_CARD_EXPIRY, card_expiry)
            self.set_text(CheckOutLocators.ADD_CARD_CVV, card_cvv)

        if save == 'yes':
            self.click(CheckOutLocators.ADD_CARD_SAVE_BUTTON, "кнопка Сохранить")
        else:
            self.click(CheckOutLocators.ADD_CARD_SAVE_CHECK_BOX, "декативировать чекбокс Запомнить данные карты")
            self.click(CheckOutLocators.ADD_CARD_SAVE_BUTTON, "кнопка Сохранить")

    @allure.step("Проверить наличие кнопки 'Добавить карту +'")
    def check_btn_add_card(self):
        self.is_element_present(CheckOutLocators.ADD_NEW_CARD_PLUS)

    @allure.step("Добавление адреса доставки")
    def add_main_address(self):
        # with allure.step('Нажать кнопку "Добавить адрес"'):
        #     self.click(CheckOutLocators.ADD_ADDRESS_BUTTON)
        with allure.step('Ввести значение в поле "Город"'):
            self.set_text(CheckOutLocators.ADD_ADDRESS_CITY, valid_city)
        with allure.step('Выбрать город из всплывашки'):
            self.click(CheckOutLocators.ADD_ADDRESS_POPUP)
        with allure.step('Ввести значение в поле "Улица"'):
            self.set_text(CheckOutLocators.ADD_ADDRESS_STREET, valid_street)
        with allure.step('Выбрать улицу из всплывашки'):
            self.click(CheckOutLocators.ADD_ADDRESS_POPUP)
        with allure.step('Ввести значение в поле "Квартира"'):
            self.set_text(CheckOutLocators.ADD_ADDRESS_APARTMENT, valid_apartment)
        self.get_screen()
        with allure.step('Нажать кнопку "Сохранить"'):
            self.click(CheckOutLocators.ADD_ADDRESS_SAVE_BUTTON)

    @allure.step("Проверить элементы модального окна 'ДОБАВИТЬ КАРТУ'")
    def elements_add_card(self):
        assert self.get_text(CheckOutLocators.ADD_CARD_TITLE) == 'ДОБАВИТЬ КАРТУ'
        assert self.get_text(CheckOutLocators.ADD_CARD_NUMBER) == 'Номер карты'
        assert self.get_text(CheckOutLocators.ADD_CARD_OWNER) == 'Владелец карты'
        assert self.get_text(CheckOutLocators.ADD_CARD_EXPIRY) == 'Месяц / год'
        assert self.get_text(CheckOutLocators.ADD_CARD_CVV) == 'CVV / CVC'
        assert self.get_text(CheckOutLocators.ADD_CARD_SAVE_CHECK_BOX) == 'Запомнить данные карты'
        assert self.get_text(CheckOutLocators.ADD_CARD_SAVE_BUTTON) == 'СОХРАНИТЬ'
        self.get_screen()

    @allure.step("Установка даты и времени доставки")
    def set_date_and_time(self):
        if len(self.get_element(CheckOutLocators.date).all()) > 0:
            self.swipe_page_up()
            self.wait_a_second()
            self.click(CheckOutLocators.date)
            self.wait_a_moment()
            self.click(CheckOutLocators.time)

    @allure.step("Выбор способа оплаты - Подарочной картой. С заполнением данных")
    def set_gift_card(self, price):
        dictionary = gift_card_list
        gift_card_number = ''
        gift_card_pin = ''

        for i in range(len(dictionary)):
            self.set_text(CheckOutLocators.gift_card_number_field, list(dictionary.keys())[i], "Номер подарочной карты")
            self.wait_a_second()
            card_balance = self.get_number_from_element(CheckOutLocators.gift_card_balance)

            if int(price) <= card_balance:
                self.set_text(CheckOutLocators.gift_card_pin_field, list(dictionary.values())[i], "Пин-код")
                self.wait_a_second()
                self.click(CheckOutLocators.gift_card_continue_btn, "кнопка Продолжить")
                gift_card_number = list(dictionary.keys())[i]
                gift_card_pin = list(dictionary.values())[i]
                break

        with allure.step(f"Проверка наличия номера подарочной карты '{gift_card_number}'"):
            self.wait_element(CheckOutLocators.gift_number_text)
            self.d(resourceId='ru.limeshop.android.dev:id/payment_gift_number_text',
                   text=f'Подарочная карта••••{gift_card_number}')
        return gift_card_number, gift_card_pin

    @allure.step("Выбор способа доставки - Самовывоз")
    def set_pickup(self):
        self.click(CheckOutLocators.pickup_selector, "самовывоз")
        self.wait_element(CheckOutLocators.permission_while_using_the_app)
        self.click(CheckOutLocators.permission_while_using_the_app)

    @allure.step("Выбор способа оплаты - При получении")
    def set_upon_receipt(self):
        self.click(CheckOutLocators.receiving_selector, "При получении")
        self.wait_a_second()
        assert self.get_text(CheckOutLocators.PAYMENT_INFO_TEXT) == 'Наличными или картой при получении'
        self.get_screen()

    @allure.step("Выбор способа оплаты - Подарочной картой")
    def set_gift_card_selector(self):
        self.click(CheckOutLocators.gift_card_selector, "Подарочной картой")
        self.wait_element(CheckOutLocators.add_gift_card_title, "Добавить подарочную карту")

    @allure.step("Закрытие блока подарочной карты кликом мимо области блока")
    def close_gift_card_block(self):
        self.coordinate_click(500, 300)
        self.wait_hidden_element(CheckOutLocators.add_gift_card_title, 'блок добавления подарочной карты')
        self.wait_element(CheckOutLocators.add_gift_card_btn, "кнопка Добавить карту")

    @allure.step("Закрытие блока подарочной карты свайпом шторки вниз")
    def close_gift_card_block2(self):
        with allure.step("Свайп вниз блока подарочной карты"):
            gift_card_dragger_view_x = self.get_element(CheckOutLocators.gift_card_dragger_view).center()[0]
            gift_card_dragger_view_y = self.get_element(CheckOutLocators.gift_card_dragger_view).center()[1]
            d.swipe(gift_card_dragger_view_x, gift_card_dragger_view_y, gift_card_dragger_view_x,
                    gift_card_dragger_view_y + 300)
        self.wait_hidden_element(CheckOutLocators.add_gift_card_title, 'блок добавления подарочной карты')
        self.wait_element(CheckOutLocators.add_gift_card_btn, "кнопка Добавить карту")

    @allure.step("Проверка номера подарочной карты. Проверка кнопки Продолжить")
    def checking_gift_card_number(self, price):
        dictionary = gift_card_list
        self.wait_element(CheckOutLocators.gift_card_number_field)
        self.set_text(CheckOutLocators.gift_card_number_field, list(dictionary.keys())[0], "Номер подарочной карты")
        self.wait_element(CheckOutLocators.gift_card_balance, "баланс подарочной карты")
        assert self.d(text="ПРОДОЛЖИТЬ", enabled='false').wait(5) == True, print("Кнопка Продолжить Активна")
        self.set_text(CheckOutLocators.gift_card_number_field, '1234567890123456', "Номер подарочной карты")
        self.wait_element(CheckOutLocators.gift_card_balance, "баланс подарочной карты")
        self.wait_text('Неправильно указан номер карты')
        assert self.d(text="ПРОДОЛЖИТЬ", enabled='false').wait(5) == True, print("Кнопка Продолжить Активна")

    @allure.step("Проверка поля пин-код. Проверка кнопки Продолжить")
    def checking_gift_card_pin_code(self, price):
        gift_card_pin = ''
        dictionary = gift_card_list

        for i in range(len(dictionary)):
            self.set_text(CheckOutLocators.gift_card_number_field, list(dictionary.keys())[i], "Номер подарочной карты")
            self.wait_a_second()
            card_balance = self.get_number_from_element(CheckOutLocators.gift_card_balance)

            if int(price) <= card_balance:
                gift_card_pin = list(dictionary.values())[i]
                break

        self.wait_element(CheckOutLocators.gift_card_balance, "баланс подарочной карты")
        self.wait_text(price)
        self.set_text(CheckOutLocators.gift_card_pin_field, gift_card_pin, "Пин-код")
        assert self.d(text="ПРОДОЛЖИТЬ", enabled='true').wait(5) == True, print("Кнопка Продолжить неактивна")
        # self.set_text(CheckOutLocators.gift_card_number_field, list(blocked_gift_card.keys())[0], "Номер подарочной карты")
        # self.wait_element(CheckOutLocators.gift_card_balance, "баланс подарочной карты")
        # self.set_text(CheckOutLocators.gift_card_pin_field, '1234', "Пин-код")
        # self.wait_text('Не верный пин-код подарочной карты')
        # assert self.d(text="ПРОДОЛЖИТЬ", enabled='false').wait(5) == True, print("Кнопка Продолжить Активна")
        self.wait_a_second()
        self.set_text(CheckOutLocators.gift_card_pin_field, "", "Пин-код")
        assert self.d(text="ПРОДОЛЖИТЬ", enabled='false').wait(5) == True, print("Кнопка Продолжить Активна")

    @allure.step("Выбор способа оплаты - Подарочной картой. С заполнением данных и выбор доплаты")
    def set_gift_card_with_additional_payment(self, price):
        dictionary = gift_card_list
        gift_card_number = ''
        gift_card_pin = ''

        for i in range(len(dictionary)):
            self.set_text(CheckOutLocators.gift_card_number_field, list(dictionary.keys())[i], "Номер подарочной карты")
            self.wait_a_second()
            card_balance = self.get_number_from_element(CheckOutLocators.gift_card_balance)

            if int(price) <= card_balance:
                self.set_text(CheckOutLocators.gift_card_pin_field, list(dictionary.values())[i], "Пин-код")
                self.wait_a_second()
                self.set_text(CheckOutLocators.gift_card_sum_field, "200", "Сумма к списанию")
                self.wait_a_second()
                self.click(CheckOutLocators.gift_card_continue_btn, "кнопка Продолжить")
                gift_card_number = list(dictionary.keys())[i]
                gift_card_pin = list(dictionary.values())[i]
                break

        # self.wait_element(CheckOutLocators.gift_number_text)
        return gift_card_number, gift_card_pin

    @allure.step("Добавление доплаты картой")
    def add_additional_payment_no_card(self):
        self.wait_a_second()
        self.click(CheckOutLocators.payment_add_card_btn, "кнопка для добавления доплаты")
        self.wait_a_second()
        if self.is_element_present(CheckOutLocators.ADD_NEW_CARD_BUTTON):
            self.click(CheckOutLocators.ADD_NEW_CARD_BUTTON, 'кнопка добавить карту')
        else:
            self.click(self.d(textContains='Картой онлайн').sibling(resourceId='ru.limeshop.android.dev:id/is_selected_card_radio'), "способ доплаты - Картой онлайн")
        self.enter_card_data()
        self.check_additional_payment()

    @allure.step("Добавление доплаты картой")
    def add_additional_payment(self):
        self.wait_a_second()
        self.click(CheckOutLocators.payment_add_card_btn, "кнопка для добавления доплаты")
        self.wait_a_second()
        if self.is_element_present(CheckOutLocators.ADD_NEW_CARD_BUTTON):
            self.click(CheckOutLocators.ADD_NEW_CARD_BUTTON, 'кнопка добавить карту')
        else:
            self.click(self.d(textContains='Добавить карту').sibling(resourceId='ru.limeshop.android.dev:id/is_selected_card_radio'), "способ доплаты - Картой онлайн")
        self.enter_card_data()
        self.check_additional_payment()

    @allure.step("Заполнить данные карты")
    def enter_card_data(self, card=card_1):
        self.set_text(CheckOutLocators.card_number, card, "номер карты")
        self.set_text(CheckOutLocators.cardholder, card_owner, "владелец карты")
        self.set_text(CheckOutLocators.card_date, card_expiry, "дата окончания карты")
        self.set_text(CheckOutLocators.card_cvv, card_cvv, "cvv карты")
        self.click(CheckOutLocators.save_card_btn, "кнопка Сохранить")

    @allure.step("Проверить что карта добавлена в способ доплаты")
    def check_additional_payment(self):
        if len(self.d.xpath('//*[@text="СПОСОБ ДОПЛАТЫ"]').all()) > 0:
            self.coordinate_click(100, 100)
        self.wait_a_second()
        assert self.d(resourceId='ru.limeshop.android.dev:id/payment_card_number_text', textContains='4242').wait(
            5) == True, print("В блоке Доплата не отображается карта 4242")

    @allure.step("Добавление доплаты картой")
    def add_additional_payment_sbp(self):
        self.wait_a_second()
        self.click(CheckOutLocators.payment_add_card_btn, "кнопка для добавления доплаты")
        self.wait_element('ru.limeshop.android.dev:id/is_selected_card_radio')
        self.click(self.d(textContains='Через СБП').sibling(
            resourceId='ru.limeshop.android.dev:id/is_selected_card_radio'), "способ доплаты - СБП")
        self.wait_element(CheckOutLocators.CARD_INFO)
        assert self.get_text(CheckOutLocators.CARD_INFO) == 'Через СБП', print(
            'В блоке Доплата не отображается Через СБП')

    @allure.step("Клик Продолжить покупки (после оформления заказа)")
    def click_continue_shopping(self):
        self.wait_element(SuccessPayScreenLocators.BUTTON)
        self.click(SuccessPayScreenLocators.BUTTON, "кнопка Продолжить покупки")

    @allure.step("Проверка наличия номера карты '{card_number}' в чекауте")
    def checking_payment_card_number(self, card_number):
        self.click(CheckOutLocators.card_online_selector)
        assert self.d(resourceId='ru.limeshop.android.dev:id/payment_card_number_text',
                      textContains=f'{card_number}').wait(5) == True, print(f"Не отображается карта {card_number}")

    @allure.step("Проверка наличия номера карты '{card_number}' на экране Ваши карты")
    def checking_card_list(self, card_number):
        assert self.d(resourceId='ru.limeshop.android.dev:id/info_text_view', textContains=f'{card_number}').wait(
            5) == True, print(f"Не отображается карта {card_number}")

    # @allure.step("Добавление адреса доставки")
    # def add_courier_address(self):
    #     self.click(CheckOutLocators.add_courier_address_btn, "кнопка Добавить адрес")
    #     self.set_text(CheckOutLocators.city, "Новосибирск", "город")
    #     self.wait_element(CheckOutLocators.address_popup)
    #     self.click(CheckOutLocators.address_popup)
    #     self.set_text(CheckOutLocators.street, "Иванова 1", "улица")
    #     self.wait_element(CheckOutLocators.address_popup)
    #     self.click(CheckOutLocators.address_popup)
    #     self.set_text(CheckOutLocators.apartment, "1", "квартира")
    #     self.click(CheckOutLocators.save_address_btn, "кнопка Сохранить")
    #     self.wait_text("ОФОРМЛЕНИЕ ЗАКАЗА")

    @allure.step("Нажать кнопку 'Добавить адрес'")
    def click_add_address_btn(self):
        self.wait_element(CheckOutLocators.add_courier_address_btn)
        self.click(CheckOutLocators.add_courier_address_btn, "кнопка Добавить адрес")

    @allure.step("Проверить элементы окна 'ДОБАВИТЬ АДРЕС'")
    def elements_add_address(self):
        assert self.get_text(CheckOutLocators.ADD_ADDRESS_TITLE) == 'ДОБАВИТЬ АДРЕС'
        assert self.get_text(CheckOutLocators.ADD_ADDRESS_SAVE_BUTTON) == 'СОХРАНИТЬ'
        self.wait_text(valid_name_kir)
        self.wait_text(valid_surname_kir)
        self.wait_text('+7 963 944 78 45')
        # self.wait_text(email)

    @allure.step("Выбрать способ доставки 'КУРЬЕРОМ'")
    def courier_select(self):
        self.click(CheckOutLocators.courier_selector, "Курьером")

    @allure.step("Выбрать способ доставки 'САМОВЫВОЗ'")
    def pickup_select(self):
        self.click(CheckOutLocators.pickup_selector, "Самовывоз")

    @allure.step("Выбрать способ оплаты 'КАРТОЙ ОНЛАЙН'")
    def card_online_select(self):
        self.click(CheckOutLocators.card_online_selector, "КАРТОЙ ОНЛАЙН")

    @allure.step("Выбрать способ оплаты 'ЧЕРЕЗ СБП'")
    def sbp_select(self):
        self.click(CheckOutLocators.sbp_selector, "ЧЕРЕЗ СБП")

    @allure.step("Выбрать способ оплаты 'ПОДАРОЧНОЙ КАРТОЙ'")
    def gift_card_select(self):
        self.click(CheckOutLocators.gift_card_selector, "ПОДАРОЧНОЙ КАРТОЙ")

    @allure.step("Выбрать способ оплаты 'ПРИ ПОЛУЧЕНИИ'")
    def receiving_select(self):
        self.click(CheckOutLocators.receiving_selector, "ПРИ ПОЛУЧЕНИИ")

    @allure.step("Разрешить доступ к геолокации 'При использовании приложения'")
    def allow_access_geo(self):
        element = self.d.xpath(PermissionGeoLocators.allow_foreground_only_button).wait(timeout=5)
        if element is not None:
            self.d.xpath(PermissionGeoLocators.allow_foreground_only_button).click()

    @allure.step("Разрешить доступ к геолокации 'Однократно'")
    def allow_access_geo_one_time(self):
        element = self.d.xpath(PermissionGeoLocators.allow_one_time_button).wait(timeout=5)
        if element is not None:
            self.d.xpath(PermissionGeoLocators.allow_one_time_button).click()

    @allure.step("Переключить вкладку 'Самовывоз - Список'")
    def tab_list_select(self):
        self.click(PickupLocators.tab_list, "список")

    @allure.step("Выбрать ПВЗ")
    def pickup_select_pvz(self):
        self.pickup_select()
        self.wait_a_second()
        self.allow_access_geo_one_time()
        self.tab_list_select()
        self.set_text(PickupLocators.search_field, 'Новосибирск')
        self.wait_a_second()
        self.click(CheckOutLocators.ADD_ADDRESS_POPUP)
        self.wait_a_second()
        self.wait_element(PickupLocators.order_here_button)
        element = self.get_random_element(PickupLocators.order_here_button)
        self.click(element)

    @allure.step("Нажать иконку раскрывающегося списка 'Состав заказа'")
    def open_order_list(self):
        self.click(CheckOutLocators.ORDER_LIST_SHEVRON)

    @allure.step('Стоимость товара с учетом скидки в карточке Состав заказа')
    def get_order_list_price_with_discount(self):
        return self.get_number_from_element(CheckOutLocators.order_list_price_with_sale)

    @allure.step('Суммарная скидка')
    def get_summary_discount(self):
        return self.get_number_from_element(CheckOutLocators.summary_discount)

    @allure.step('Суммарная стоимость (Без скидки)')
    def get_summary_coast(self):
        return self.get_number_from_element(CheckOutLocators.SUMMARY_COAST)

    @allure.step('Суммарная стоимость c учетом скидки в блоке саммери')
    def get_summary_total(self):
        return self.get_number_from_element(CheckOutLocators.SUMMARY_TOTAL)

    @allure.step('Суммарная стоимость c учетом скидки в блоке саммери')
    def check_discount(self, price, discount, price_with_discount):
        price_order_list = self.get_order_list_price_with_discount()
        assert price_order_list == price_with_discount, f'Итоговая цена из корзины{price_with_discount} не совпадает с ценой в составе заказа {price_order_list}'
        summary_discount = self.get_summary_discount()
        assert discount == summary_discount, f"Скидка с экрана Корзина {discount} не совпадает со скидкой на экране Оформление заказа {summary_discount}"
        summary_coast = self.get_summary_coast()
        summary_total = self.get_summary_total()
        assert price == summary_coast, f'Стоимость с карточки товара {price} не совпадает с стоимостью в блоке саммери {summary_coast}'
        assert price_with_discount == summary_total, f'Стоимость товара со скидкой {price_with_discount} с экрана корзина не совпадает с стоимостью со скидкой в блоке саммери {summary_total}'

