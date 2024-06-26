import time

import allure
import pytest

from config import product_name_ru
from locators import SearchLocators, FavoritesLocators, MainLocators, CatalogLocators, CollectionLocators, \
    ProductCardLocators, CartLocators, ProfileLocators
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Smoke")
class TestSmoke:
    @pytest.mark.search
    @allure.title('Экран "Поиск" / Удачный поиск по текстовому запросу')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2227")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2229")
    def test_search_text(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.checking_search_elements()
        page.search.entering_search_query(product_name_ru)
        page.search.checking_elements_after_search()

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Удачный поиск по артикулу')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2230")
    def test_article_search(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.click_colors()
        article = page.card.get_article()
        page.press_back()
        page.open_search()
        page.search.entering_search_query(article)
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        page.search.open_found_card()
        page.card.checking_article_in_found_card(article)

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Добавление в избранное из результатов поиска')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2231")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2235")
    def test_adding_found_card_to_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("Платье")
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        card_name = page.search.get_card_name()
        page.search.open_found_card()
        assert card_name == page.card.get_product_name(), f"Карточка в поиске не соответствует открытой карточке. В поиске - {card_name}, открытая карточка - {page.card.get_product_name()}"
        page.card.add_to_favorites()
        page.press_back()
        page.open_favorites()
        page.favorites.checking_availability_cards(card_name)

    @pytest.mark.smoke
    @allure.title('Экран "Поиск" / Добавление в избранное из результатов поиска (иконка в ячейке)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2232")
    def test_adding_found_card_to_favorites_from_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_search()
        page.search.entering_search_query("Платье")
        page.wait_element(SearchLocators.card_name_in_search_result, "найденная по запросу карточка")
        card_name = page.search.add_to_favorite()
        page.wait_a_second()
        page.click_x()
        page.open_favorites()
        page.favorites.checking_availability_cards(card_name)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Пустой список')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2236")
    def test_empty_favorites_screen(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.wait_element(FavoritesLocators.BUTTONBUY)
        page.favorites.wait_element(FavoritesLocators.INFOTEXT)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Товар в избранном')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2237")
    def test_product_in_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.delete_from_favorites()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.wait_text(product_name)
        page.wait_element(FavoritesLocators.BUTTONBUYSTUFF)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Удаление товара из избранного')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/2238")
    def test_delete_product_from_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.delete_from_favorites()
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.click(FavoritesLocators.BOTTONDELETEFROMFAV)
        page.wait_a_second()
        page.favorites.wait_hidden_element(FavoritesLocators.BUTTONBUYSTUFF)
        page.favorites.wait_element(FavoritesLocators.INFOTEXT)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Кнопка "Купить" для товара')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/2239')
    def test_bottom_buy_for_favorites_product(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.favorites_product_bottom_buy()

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Добавить товар в корзину')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/2240')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/2241')
    def test_add_to_cart(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = [page.card.add_to_favorites()]
        page.click_x()
        page.open_favorites()
        page.favorites.add_to_cart_and_go_to_cart()
        page.cart.checking_availability_cards(product_name)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Переход на экран "Корзина"(Через ТапБар)')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/233')
    def test_add_to_cart_from_navbar(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = [page.card.add_to_favorites()]
        page.click_x()
        page.open_favorites()
        page.favorites.add_to_cart()
        page.open_cart()
        page.cart.checking_availability_cards(product_name)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Добавление товара в корзину')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/10')
    def test_add_to_cart(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product_name = [page.card.add_to_favorites()]
        page.click_x()
        page.open_favorites()
        page.favorites.add_to_cart_and_go_to_cart()
        page.cart.checking_availability_cards(product_name)

    @pytest.mark.smoke
    @allure.title('Экран "Избранное" / Закрытие экрана "Избранное"')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/238')
    def test_close_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.click_x()
        page.wait_hidden_element(FavoritesLocators.TITLE, 'Заголовок "Избраное"')
        page.wait_hidden_element(FavoritesLocators.BUTTONBUYSTUFF, 'Кнопка "Начать покупки"')

    @pytest.mark.smoke
    @allure.title('Переход в карточку товара и выход из нее')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/241')
    @allure.testcase('https://lmdev.testrail.io/index.php?/cases/view/276')
    def test_go_to_card(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.add_to_favorites()
        page.click_x()
        page.open_favorites()
        page.favorites.go_to_card()
        page.click_x()

    @pytest.mark.smoke
    @allure.title('Экран "Каталог" / Переход из каталога на основной экран')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1757")
    def test_close_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.click_x()
        page.wait_hidden_element(CatalogLocators.catalog_item)
        page.wait_element(MainLocators.lime_logo)
        page.wait_hidden_element(CatalogLocators.MENU_ITEM)

    @pytest.mark.smoke
    @allure.title('Экран "Каталог" / Основной раздел')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/53")
    def test_open_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.wait_element(CatalogLocators.WOMEN)
        page.wait_element(CatalogLocators.KIDS)
        page.wait_element(CatalogLocators.MEN)
        page.wait_element(MainLocators.X_BUTTON, 'Кнопка "Назад"')
        catalog_list = page.catalog.get_element(CatalogLocators.catalog_item).count
        assert catalog_list >= 1, print(f"Разделы каталогов не найдены. Catalog_list = {catalog_list}")
        page.swipe_page_up()
        page.wait_element(CatalogLocators.GIFT_CARD, 'Подарочная карта')

    @pytest.mark.smoke
    @allure.title('Экран "Каталог" / Раздел без подразделов')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/54")
    def test_catalog_without_chapter(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_catalog_without_chapter()

    @pytest.mark.smoke
    @allure.title('Экран "Каталог" / Переход от раздела к разделу(Содержащий подразделы)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/54")
    def test_catalog_with_chapter(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        catalog_name = page.catalog.open_catalog_with_chapter()
        print(f"{catalog_name}.Содержит разделы")

    @pytest.mark.smoke
    @allure.title('Экран "Каталог" / Клик по ячейке пункта меню')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/3221")
    def test_tap_out_name_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.click_catalog_coords()
        if page.catalog.get_element(CatalogLocators.catalog_item_recycler).count == 0:
            page.wait_element(CollectionLocators.title)

    @pytest.mark.smoke
    @allure.title('Экран "Каталог" / Переход из пустого избранноего')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/2585")
    def test_tap_out_name_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.click(FavoritesLocators.BUTTONBUY)
        page.catalog.wait_element(CatalogLocators.WOMEN)
        page.catalog.wait_element(CatalogLocators.MEN)
        page.catalog.wait_element(CatalogLocators.KIDS)
        page.catalog.wait_element(CatalogLocators.catalog_item)

    @pytest.mark.smoke
    @allure.title('Экран "Каталог" / Переключения между категориями')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1756")
    def test_change_chapter(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.change_chapter()

    @pytest.mark.smoke
    @allure.title('Экран "Каталог" / Переход из пустого экрана "Избранное"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/2585")
    def test_open_catalog_from_favorites(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_favorites()
        page.favorites.click(FavoritesLocators.BUTTONBUY)
        page.wait_element(CatalogLocators.catalog_item, "Коллекции")
        page.wait_hidden_element(FavoritesLocators.TITLE)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Выход с экрана')
    @allure.title('Экран "Коллекции" / Переход на экран')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/3391")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/483")
    def test_bottom_back(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.wait_element(CollectionLocators.title)
        page.click_x()
        page.wait_hidden_element(CollectionLocators.title)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Баннер в коллекции (фото)')
    @allure.title('Экран "Коллекции" / Баннер в коллекции (клик на баннер)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/213")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/336")
    def test_click_for_photobanner(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.click('//*[@text="КОЛЛЕКЦИЯ STUDIO"]')
        page.click('//*[@text="ВСЕ МОДЕЛИ"]')
        page.wait_element(CollectionLocators.banner_image, "Фотобаннер отображается")
        page.click(CollectionLocators.banner_image)
        page.wait_hidden_element(CollectionLocators.banner_image)
        page.wait_element(CollectionLocators.cards_image)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Фильтр коллекции товара')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/484")
    def test_filter_bottom(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.wait_element(CollectionLocators.filters_btn)
        page.click(CollectionLocators.filters_btn)
        page.wait_element(CollectionLocators.filter_price_asc_cbox)
        page.wait_element(CollectionLocators.color_box_1)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Переход к карточке товара')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/286")
    def test_open_card(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.wait_element(ProductCardLocators.product_name)
        page.card.wait_element(ProductCardLocators.product_price)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Добавление в избранное (добавление в список) с экрана "Коллекция"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/283")
    def test_add_to_favorites_from_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        product_price, product_name = page.catalog.add_to_favorites_from_catalog()
        page.click(MainLocators.FAVORITES_NAV)
        favorites_name = page.get_text(FavoritesLocators.STUFFNAME)
        favorites_price = page.get_number_from_element(FavoritesLocators.STUFFPRICE)
        assert favorites_price == product_price, print("Цена отличается")
        assert favorites_name == product_name, print(f"Название товара отличается, {favorites_name},{product_name}")

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" /Удаление из избранного (удаление из списка) с экрана "Коллекция"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/284")
    def test_del_to_favorites_from_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.click(CatalogLocators.cards_image)
        page.card.add_to_favorites()
        card_name = page.card.get_product_name()
        page.card.click(ProductCardLocators.back_btn)
        page.click(MainLocators.FAVORITES_NAV)
        page.favorites.checking_availability_cards(card_name)
        page.click(MainLocators.CATALOG_NAV)
        page.catalog.add_to_favorites_from_catalog()
        page.click(MainLocators.FAVORITES_NAV)
        page.wait_element(FavoritesLocators.BUTTONBUY)
        page.wait_element(FavoritesLocators.INFOTEXT)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Добавление в избранное нескольких товаров (более 3-х) с экрана "Коллекция"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/3101")
    def test_add_a_few_to_favorites_from_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        product_list = page.catalog.add_a_few_to_favorites_from_catalog()
        page.click(MainLocators.FAVORITES_NAV)
        page.favorites.checking_availability_cards(product_list)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Отображение добавленного в избранное (из карточки)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1977")
    def test_equals_favorites_icon_card_and_catalog(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_card()
        page.card.add_to_favorites()
        page.card.click_back()
        color = page.get_color(CollectionLocators.FAVORITEBUTTON)
        assert color == (0, 0, 0), "Цвет не черный - Товар не добавлен в избранное"

    @pytest.mark.smoke
    @allure.title('Экран "Коллекция" / Переход на экран "Фильтр"(Android)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/488")
    def test_open_filters_screen(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.click(CollectionLocators.filters_btn)
        page.wait_element(CollectionLocators.filter_price_asc_cbox)
        page.wait_element(CollectionLocators.color_box_1)

    #@pytest.mark.smoke
    #@allure.title('Экран "Фильтр" / Комбинированная фильтрация')
    #@allure.title("https://lmdev.testrail.io/index.php?/cases/view/1668")
    #def test_combine_filtration(self, connect_to_device):
    #    page = MainPage(connect_to_device)
    #    page.open_catalog()
    #    page.catalog.open_random_catalog()
    #    page.click(CollectionLocators.filters_btn)
    #    page.catalog.combine_filtration()

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Открыть карточку товара')
    @allure.title('Экран "Карточка товара" / Кнопка возврата')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/288")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/11")
    def test_open_card(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.wait_element(ProductCardLocators.product_name)
        page.card.wait_element(ProductCardLocators.product_price)
        page.card.wait_element(ProductCardLocators.FAVORITE)
        page.card.wait_element(ProductCardLocators.BUY)
        page.card.click_back()
        page.catalog.wait_element(CollectionLocators.title)
        page.catalog.wait_element(CollectionLocators.CARDPRICE)
        page.catalog.wait_element(CollectionLocators.filters_btn)

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Открыть шторку (Расширенный экран информации о товаре)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/290")
    def test_open_advanced_menu_of_product(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.swipe_in_card()
        page.card.checking_advanced_info_card()

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Кнопка "Купить"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/12")
    def test_bottom_buy(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.click(ProductCardLocators.BUY)
        page.card.checking_modal_screen()

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Кнопка "Избранное" (Добавить в избранное)')
    @allure.title('Экран "Карточка товара" / Кнопка "Избранное" (Удалить из избранного)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/291")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/293")
    def test_add_to_favorites_and_del(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product = page.card.add_to_favorites()
        page.card.click_back()
        page.click(MainLocators.FAVORITES_NAV)
        page.favorites.checking_availability_cards(product)
        page.favorites.click(FavoritesLocators.STUFF)
        page.card.click(ProductCardLocators.FAVORITE)
        page.card.click_back()
        page.favorites.wait_element(FavoritesLocators.TITLE)
        page.favorites.wait_element(FavoritesLocators.INFOTEXT)
        page.favorites.wait_hidden_element(FavoritesLocators.STUFF)

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Кнопка "Корзина"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/294")
    def test_cart_bottom_from_card(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product = page.card.get_element(ProductCardLocators.product_name)
        page.card.click(ProductCardLocators.CART)
        page.cart.wait_hidden_element(product)

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / ЗУМ (Переход с первого фото)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/325")
    def test_zoom_card(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        bounds = page.card.get_element(ProductCardLocators.PHOTO_ZOOM).bounds[3]
        page.card.zoom_image()
        bounds_zoom = page.card.get_element(ProductCardLocators.ZOOM_VIEW).bounds[3]
        assert bounds < bounds_zoom
        page.card.wait_hidden_element(ProductCardLocators.product_name)
        page.card.wait_hidden_element(ProductCardLocators.product_price)

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Добавление товара в корзину(Плашка)')
    @allure.title('Экран "Карточка товара" / Добавление нескольких товаров в корзину подряд (Плашка)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/2943")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/2606")
    def test_snack_bar_when_buy_product(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        page.card.click(ProductCardLocators.BUY)
        page.card.click(ProductCardLocators.SIZES_PRODUCT)
        page.card.buy_a_few_product()

    @pytest.mark.smoke
    @allure.title('Экран "Карточка товара" / Переход в корзину(Плашка)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/2944")
    def test_snack_bar_when_buy_product(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_catalog()
        page.catalog.open_random_catalog()
        page.catalog.open_random_card()
        product = page.card.get_text(ProductCardLocators.product_name)
        page.card.click(ProductCardLocators.BUY)
        page.card.click(ProductCardLocators.SIZES_PRODUCT)
        page.card.click(ProductCardLocators.POPUP_BUTTON)
        page.cart.wait_element(CartLocators.TITLE)
        cart_product = page.cart.get_text(CartLocators.PRODUCT_TITLE)
        assert product == cart_product

    @pytest.mark.smoke
    @allure.title('Экран "Личный кабинет" / Экран "Личный кабинет" (Пользователь не авторизован)')
    @allure.title('Экран "Личный кабинет" / Выход с экрана')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/16")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/317")
    def test_open_profile_and_quit(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.checking_account_elements()
        page.profile.exit_from_profile()

    @pytest.mark.smoke
    @allure.title('Экран "Личный кабинет" / Кнопка "Руководство по покупке"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/318")
    def test_open_how_to_buy(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.open_manual()

    @pytest.mark.smoke
    @allure.title('Экран "Личный кабинет" / Кнопка "Контакты"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/319")
    def test_open_how_to_buy(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.open_contacts()

    @pytest.mark.smoke
    @allure.title('Экран "Личный кабинет"  / Кнопка "Компания"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/320")
    def test_open_company(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.open_company()

    @pytest.mark.smoke
    @allure.title('Экран "Личный кабинет" / Кнопка "Магазины"(геолокация включена)')
    @allure.title('Экран "Личный кабинет" / Кнопка "Магазины"(назад)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/2053")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/3247")
    def test_open_company(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.open_shops()
        page.profile.checking_shops_elements()
        page.click_x()
        page.profile.checking_account_elements()

    @pytest.mark.smoke
    @allure.title('Экран "Личный Кабинет" / Кнопка "Подписки и Уведомления"')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1822")
    def test_open_subscriptions_and_notifications(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.open_subscribed_screen()

    @pytest.mark.smoke
    @allure.title('Экран "Личный кабинет" / Кнопка "Условия покупки"')
    @allure.title('Экран "Личный кабинет" / Кнопка "Условия покупки"(назад)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1982")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1983")
    def test_open_terms_of_purchase(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.swipe_page_up(2)
        page.profile.click(ProfileLocators.TERMS_OF_PURCHASE)
        time.sleep(3)
        page.wait_element(ProfileLocators.OFFER_DOCUMENT)
        page.click(ProfileLocators.BTN_BACK_TERMS)
        page.profile.checking_account_elements()

    @pytest.mark.smoke
    @allure.title('Экран "Личный кабинет" / Кнопка "Политика конфиденциальности"')
    @allure.title('Экран "Личный кабинет" / Кнопка "Политика конфиденциальности"(назад)')
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1984")
    @allure.title("https://lmdev.testrail.io/index.php?/cases/view/1985")
    def test_open_privacy_policy(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.swipe_page_up(2)
        page.profile.click(ProfileLocators.PRIVACY_POLICY)
        time.sleep(3)
        page.wait_element(ProfileLocators.PRIVACY_POLICY_DOCUMENT)
        page.click(ProfileLocators.PRIVACY_POLICY_BTN_BACK)
        page.profile.checking_account_elements()






