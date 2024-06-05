import time
import allure
from pages.base_page import BasePage
from locators import *
from config import *


class ProductCardPage(BasePage):

    @allure.step('Клик по кнопке "Купить"')
    def add_to_cart(self):
        self.click(ProductCardLocators.BUY, "кнопка Купить")
        self.wait_a_moment()

    def elements_product_card(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(ProductCardLocators.BUY) == 'КУПИТЬ'
        assert self.get_text(ProductCardLocators.COLORS) == 'Цвета'
        self.get_screen()

    @allure.step("Проверка наличия элементов карточки товара")
    def checking_card_elements(self):
        self.wait_element(ProductCardLocators.BUY, "Купить")
        self.wait_element(ProductCardLocators.FAVORITE, "Избранное")
        self.wait_element(ProductCardLocators.SHARE, "Поделиться")
        self.wait_element(ProductCardLocators.CART, "Корзина")
        self.d.swipe(self.get_element(ProductCardLocators.product_name).center()[0],
                     self.get_element(ProductCardLocators.product_name).center()[1],
                     self.get_element(ProductCardLocators.product_name).center()[0],
                     self.get_element(ProductCardLocators.product_name).center()[1] + 500)
        self.wait_element(ProductCardLocators.ART, "Артикул")
        self.wait_element(ProductCardLocators.SIZES_GUIDE, "Руководство по размерам")
        self.wait_element(ProductCardLocators.COMPOSITIONS_AND_CARE, "Состав и уход")
        self.wait_element(ProductCardLocators.DELIVERY, "Доставка и возврат")
        self.wait_element(ProductCardLocators.PRODUCT_STOCKS, "Наличие в магазинах")
        self.swipe_page_up()
        self.wait_element(ProductCardLocators.PAYMENT, "Оплата")
        # self.wait_element(ProductCardLocators.GOES_WELL)
        # self.wait_element(ProductCardLocators.YOU_LIKE_IT)
        self.get_screen()

    @allure.step("Свайп к описанию")
    def swipe_in_card(self):
        product_name_bound = self.get_element(ProductCardLocators.product_name).center()
        self.d.swipe(product_name_bound[0], product_name_bound[1], product_name_bound[0], product_name_bound[1] - 700)

    @allure.step("Выбор рандомного размера")
    def select_random_size(self):
        if len(self.get_element(ProductCardLocators.available_size).all()) > 0:
            self.get_random_element(ProductCardLocators.available_size).click()
            self.wait_a_second()
            return True
        else:
            self.press_back()
            self.press_back()

    # @allure.step("Получение цены товара")
    def get_product_price(self):
        return self.get_number_from_element(ProductCardLocators.product_price)

    @allure.step('Переход в корзину')
    def open_cart(self):
        self.click(ProductCardLocators.CART, "кнопка корзины")

    # @allure.step("Получение названия товара")
    def get_product_name(self):
        return self.get_text(ProductCardLocators.product_name)

    @allure.step('Добавление/удаление из избранного')
    def add_to_favorites(self):
        self.click(ProductCardLocators.FAVORITE, 'Кнопка добавления/удаления из избранного')
        product_name = self.get_product_name()
        return product_name

    @allure.step("Добавление в корзину второго размера одного товара")
    def add_to_cart_more_item(self, size):
        self.click(ProductCardLocators.BUY_MORE, "кнопка Купить еще")
        self.click(self.get_random_element(
            f'//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]//android.widget.TextView['
            f'@resource-id="ru.limeshop.android.dev:id/product_add_to_cart_name" and not('
            f'following-sibling::android.widget.TextView['
            f'@resource-id="ru.limeshop.android.dev:id/product_add_to_cart_available"]) and not(@text="{size}")]'),
            "рандомный размер")

    @allure.step("Клик по кнопке Назад")
    def click_back(self):
        self.click(ProductCardLocators.back_btn, "кнопка Назад")

    @allure.step("Клик по кнопке Поделиться")
    def click_share(self):
        self.click(ProductCardLocators.SHARE, "кнопка Поделиться")

    @allure.step("Клик по кнопке Доставка и возврат")
    def click_delivery(self):
        self.click(ProductCardLocators.DELIVERY, "кнопка Доставка и возврат")
        self.wait_element(ProductCardLocators.delivery_description_page, "описание доставки и возврата")
        self.wait_text("ДОСТАВКА И ВОЗВРАТ")
        self.wait_text("СРОКИ ДОСТАВКИ")

    @allure.step("Клик по кнопке Оплата")
    def click_payment(self):
        self.click(ProductCardLocators.PAYMENT, "кнопка Оплата")
        self.wait_element(ProductCardLocators.payment_url, "url страницы Оплата")

    @allure.step("Клик по кнопке Цвета")
    def click_colors(self):
        self.click(ProductCardLocators.COLORS, "кнопка Цвета")

    # @allure.step("Получение значения выбранного цвета")
    def get_selected_color(self):
        return self.get_text(ProductCardLocators.selected_color)

    @allure.step("Выбор случайного цвета")
    def select_color(self):
        random_color_element = self.get_random_element(ProductCardLocators.unselected_color)
        color = random_color_element.text
        self.click(random_color_element, "рандомный цвет")
        return color

    @allure.step("Клик по фото в карточке товара")
    def zoom_image(self):
        self.click(ProductCardLocators.PHOTO_ZOOM, "фото товара")

    @allure.step("Проверка попапа в карточке после добавления товара в корзину")
    def checking_popup_buy_btn(self):
        self.wait_element(ProductCardLocators.popup_buy_btn, "плашка добавления товара в корзину")
        assert self.get_text(ProductCardLocators.popup_title) == 'Товар добавлен в корзину', print(
            f"Текст на плашке некорректен. Полученный текст: {self.get_text(ProductCardLocators.popup_title)}, ожидаемый текст: Товар добавлен в корзину")
        self.wait_element(ProductCardLocators.popup_btn, "кнопка Перейти")

    @allure.step("Переход в корзину по кнопке Перейти в попапе")
    def click_popup_buy_btn(self):
        self.click(ProductCardLocators.popup_btn, "кнопка Перейти")

    # @allure.step("Получение артикула")
    def get_article(self):
        return self.get_text(ProductCardLocators.ART).partition(' ')[2]

    @allure.step("Проверка артикула в найденной карточке")
    def checking_article_in_found_card(self, article):
        self.click_colors()
        assert article == self.get_article(), f"Артикул найденной карточки отличается от исходника. Исходный артикул - {article}, артикул найденной карточки - {self.get_article()} "

    @allure.step('Проверка элементов на экране "Расширенная информация о товаре')
    def checking_advanced_info_card(self):
        self.wait_element(ProductCardLocators.ART, "Артикул")
        self.wait_element(ProductCardLocators.SIZES_GUIDE, "Руководство по размерам")
        self.wait_element(ProductCardLocators.COMPOSITIONS_AND_CARE, "Состав и уход")
        self.wait_element(ProductCardLocators.DELIVERY, "Доставка и возврат")
        self.wait_element(ProductCardLocators.PRODUCT_STOCKS, "Наличие в магазинах")
        self.wait_element(ProductCardLocators.PAYMENT, "Оплата")

    @allure.step('Проверка элементов в модалке "Купить"')
    def checking_modal_screen(self):
        self.wait_element(ProductCardLocators.SIZE_INFO)
        self.wait_element(ProductCardLocators.BOTTOM_SHEET)
        self.wait_element(ProductCardLocators.SIZES_PRODUCT)

    @allure.step('Покупка нескольких товаров')
    def buy_a_few_product(self):
        self.click(ProductCardLocators.BUY)
        self.click(ProductCardLocators.SIZES_PRODUCT)
        self.click(ProductCardLocators.BUY_MORE)
        self.click(ProductCardLocators.SIZES_PRODUCT)
        self.click(ProductCardLocators.BUY_MORE)
        self.click(ProductCardLocators.SIZES_PRODUCT)
        self.click(ProductCardLocators.BUY_MORE)
        self.click(ProductCardLocators.SIZES_PRODUCT)
        time.sleep(5)
        self.wait_hidden_element(ProductCardLocators.POPUP)

