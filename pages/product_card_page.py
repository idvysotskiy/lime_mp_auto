import time
import allure
from pages.base_page import BasePage
from locators import *
from config import *

BUY = '//*[@resource-id="ru.limeshop.android.dev:id/buy_button"]'
BUY_MORE = '//*[@resource-id="ru.limeshop.android.dev:id/buy_more_button"]'
COLORS = '//*[@resource-id="ru.limeshop.android.dev:id/productColorsConstraintLayout"]'
FAVORITE = '//*[@resource-id="ru.limeshop.android.dev:id/productAddToFavoritesImageButton"]'
SHARE = '//*[@resource-id="ru.limeshop.android.dev:id/productShareImageButton"]'
CART = '//*[@resource-id="ru.limeshop.android.dev:id/productCartImageButton"]'
PHOTO_ZOOM = '//*[@resource-id="ru.limeshop.android.dev:id/productPhotosViewpager"]'
ART = '//*[@resource-id="ru.limeshop.android.dev:id/productArticleTextView"]'
SIZES_GUIDE = '//*[@resource-id="ru.limeshop.android.dev:id/product_sizes_text_view"]'
COMPOSITIONS_AND_CARE = '//*[@resource-id="ru.limeshop.android.dev:id/productCompositionAndCareTextView"]'
DELIVERY = '//*[@resource-id="ru.limeshop.android.dev:id/productDeliveryTextView"]'
PRODUCT_STOCKS = '//*[@resource-id="ru.limeshop.android.dev:id/productStocksTextView"]'
PAYMENT = '//*[@resource-id="ru.limeshop.android.dev:id/productPaymentTextView"]'
GOES_WELL = '//*[@resource-id="ru.limeshop.android.dev:id/goesWellTextView"]'
YOU_LIKE_IT = '//*[@resource-id="ru.limeshop.android.dev:id/youllLikeItTextView"]'
GOES_WELL_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/goesWellRecyclerView"]/android.widget.LinearLayout[1]'
GOES_WELL_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/goesWellRecyclerView"]/android.widget.LinearLayout[2]'
YOU_LIKE_IT_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/youllLikeItRecyclerView"]/android.widget.LinearLayout[1]'
YOU_LIKE_IT_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/youllLikeItRecyclerView"]/android.widget.LinearLayout[2]'
# BOTTOM_SHEET
XS_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[1]'
S_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[2]'
M_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[3]'
L_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[4]'
XL_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[5]'
SIZE_INFO = '//*[@resource-id="ru.limeshop.android.dev:id/sizeInfoButton"]'
POPUP = '//*[@resource-id="ru.limeshop.android.dev:id/productPopup"]'
POPUP_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/popupStartTitle"]'
POPUP_BUTTON = '//*[@resource-id="ru.limeshop.android.dev:id/popupButton"]'

class ProductCardPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

    @allure.step('Нажать кнопку "Купить"')
    def add_to_cart(self):
        if self.get_text(BUY) == 'КУПИТЬ':
            self.click(BUY)
        elif self.get_text(BUY_MORE) == 'КУПИТЬ ЕЩЕ':
            self.click(BUY_MORE)

    @allure.step('Выбрать размер товара')
    def select_size(self, size):
        if size == 'XS':
            self.d.xpath(XS_SIZE).click()
        if size == 'S':
            self.d.xpath(S_SIZE).click()
        if size == 'M':
            self.d.xpath(M_SIZE).click()
        if size == 'L':
            self.d.xpath(L_SIZE).click()
        if size == 'XL':
            self.d.xpath(XS_SIZE).click()

    def elements_product_card(self):
        self.is_element_present(MainLocators.X_BUTTON)
        assert self.get_text(BUY) == 'КУПИТЬ'
        assert self.get_text(COLORS) == 'Цвета'
        BasePage(self).get_screen()

    def elements_full_product_card(self):
        assert self.get_text(BUY) == 'КУПИТЬ'
        self.is_element_present(FAVORITE)
        self.is_element_present(SHARE)
        self.is_element_present(CART)
        self.is_element_present(ART)
        self.is_element_present(SIZES_GUIDE)
        self.is_element_present(COMPOSITIONS_AND_CARE)
        self.is_element_present(DELIVERY)
        self.is_element_present(PRODUCT_STOCKS)
        self.is_element_present(PAYMENT)
        self.is_element_present(GOES_WELL)
        self.is_element_present(YOU_LIKE_IT)
        BasePage(self).get_screen()

    def open_full_product_card(self):
        self.click(COLORS)
