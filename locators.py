# file: locators.py
from config import *
import uiautomator2 as u2


# d = u2.connect(device_id)


class MainLocators:
    # BASE
    X_BUTTON = '//android.widget.ImageButton'
    NOTIFICATION_NEGATIVE = '//*[@resource-id="ru.limeshop.android.dev:id/notification_negative_button"]'
    notification_positive_button = "ru.limeshop.android.dev:id/notification_positive_button"
    TOOLBAR_TITLE = 'ru.limeshop.android.dev:id/toolbarTitle'
    lime_logo = 'ru.limeshop.android.dev:id/banner_label_image_view'
    snack_bar_message = '//*[@resource-id="ru.limeshop.android.dev:id/title_text_view"]'
    SCREENGIFTCARD = "ru.limeshop.android:id/baseContainer"
    # POPUP
    POPUP_CLEAR = '//*[@resource-id="ru.limeshop.android.dev:id/positive_button_outlined"]'
    POPUP_CANCEL = '//*[@resource-id="ru.limeshop.android.dev:id/negative_button"]'
    POPUP_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/title_text_view"]'
    POPUP_DESCRIPTION = '//*[@resource-id="ru.limeshop.android.dev:id/message_text_view"]'

    # NAV_BAR
    SEARCH_NAV = 'ru.limeshop.android.dev:id/nav_search'
    FAVORITES_NAV = 'ru.limeshop.android.dev:id/nav_favorites'
    CATALOG_NAV = 'ru.limeshop.android.dev:id/nav_catalog_menu'
    PROFILE_NAV = 'ru.limeshop.android.dev:id/nav_profile'
    CART_NAV = 'ru.limeshop.android.dev:id/nav_cart'

    # CATALOG
    FAV_ICON = 'ru.limeshop.android.dev:id/favoriteImageView'
    NAME_PRODUCT_COLLECTION = 'ru.limeshop.android.dev:id/nameTextView'
    NAME_PRODUCT_FAVORITE = 'ru.limeshop.android.dev:id/item_product_name'
    FILTER_BUTTON = '//*[@resource-id="ru.limeshop.android.dev:id/filter_menu"]'
    PRODUCT_CARD_1_1 = '//*[@resource-id="ru.limeshop.android.dev:id/recycler_catalog"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]'
    PRODUCT_CARD_2_2 = '//*[@resource-id="ru.limeshop.android.dev:id/recycler_catalog"]/android.widget.FrameLayout[2]/android.view.ViewGroup[1]'
    PRODUCT_CARD_1 = '//android.widget.TableLayout/android.widget.TableRow[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]'
    PRODUCT_CARD_2 = '//android.widget.TableLayout/android.widget.TableRow[2]/android.view.ViewGroup[2]/android.widget.FrameLayout[1]'

    registration_btn = 'ru.limeshop.android.dev:id/profile_unauthorized_signup'
    name = '//*[@text="Имя"]'
    surname = '//*[@text="Фамилия"]'
    phone = '//*[@text="Моб. телефон"]'
    email = '//*[@text="Эл. почта"]'
    password = '//*[@text="Пароль"]'
    repeat_password = '//*[@text="Повтор нового пароля"]'
    approve_checkbox = 'ru.limeshop.android.dev:id/checkable_option_active'
    continue_btn = '//*[@text="ПРОДОЛЖИТЬ"]'
    # submenu_elements_list = d(resourceId='ru.limeshop.android.dev:id/catalog_item_recycler').child(
    #     resourceId="ru.limeshop.android.dev:id/catalog_item_name")

    # CONTUR
    check_box = 'ru.limeshop.android.dev:id/item_checkable_option_active'


class SearchLocators:
    X_BUTTON = '//android.widget.ImageButton'
    TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/toolbarTitle"]'
    TEXT_EDIT = '//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    TEXT_HINT = '//*[@resource-id="ru.limeshop.android.dev:id/hintText"]'
    ICON = '//*[@resource-id="ru.limeshop.android.dev:id/startIcon"]'
    SHOPS_BTN = '//*[@resource-id="ru.limeshop.android.dev:id/topButtonsContainerLinearLayout"]/androidx.appcompat.widget.LinearLayoutCompat[1]'
    SCAN_BTH = '//*[@resource-id="ru.limeshop.android.dev:id/topButtonsContainerLinearLayout"]/androidx.appcompat.widget.LinearLayoutCompat[2]'
    SHOPS_TEXT = '//*[@text="МАГАЗИНЫ"]'
    SCAN_TEXT = '//*[@text="СКАНЕР"]'
    ALL = '//*[@text="ВСЕ"]'
    WOMAN = '//*[@text="ЖЕНЩИНЫ"]'
    MEN = '//*[@text="МУЖЧИНЫ"]'
    KIDS = '//*[@text="ДЕТИ"]'
    FIRST_RESULT_IMAGE = '//*[@resource-id="ru.limeshop.android.dev:id/searchRecyclerView"]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]'
    FIRST_RESULT_NAME = '"ru.limeshop.android.dev:id/item_product_name", text="ПЛАТЬЕ ИЗ АТЛАСА С ПРИНТОМ «ЖЕМЧУГ»"'
    FIRST_RESULT_FAV = '//*[@resource-id="ru.limeshop.android.dev:id/searchRecyclerView"]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
    ICON_FAIL_SEARCH = '//androidx.appcompat.widget.LinearLayoutCompat/android.widget.ImageView[1]'
    FAIL_SEARCH_TEXT = '//*[@text="НИЧЕГО НЕ НАЙДЕНО"]'
    FAIL_SEARCH_DESCRIPTION = '//*[@text="Проверьте, правильно ли введен запрос"]'
    card_name_in_search_result = 'ru.limeshop.android.dev:id/item_product_name'
    card_img_in_search_result = 'ru.limeshop.android.dev:id/media_view'
    card_favorite_icon = 'ru.limeshop.android.dev:id/item_product_favorite'

class CatalogLocators:
    WOMEN = '//*[@text="ЖЕНЩИНЫ"]'
    MEN = '//*[@text="МУЖЧИНЫ"]'
    KIDS = '//*[@text="ДЕТИ"]'
    EDITORIAL = '//*[@text="EDITORIAL"]'
    GIFT_CARD = '//*[@text="ПОДАРОЧНАЯ КАРТА"]'
    MENU_ITEM = "ru.limeshop.android.dev:id/catalog_item_name"
    catalog_item = 'ru.limeshop.android.dev:id/catalog_item_name'
    catalog_item_recycler = 'ru.limeshop.android.dev:id/catalog_item_recycler'
    submenu_elements_list = '//*[@resource-id="ru.limeshop.android.dev:id/catalog_item_recycler"]//*[@resource-id="ru.limeshop.android.dev:id/catalog_item_name"]'
    cards_image = "ru.limeshop.android.dev:id/media_view_container_layout"


class CollectionLocators:
    # COLLECTION
    title = "ru.limeshop.android.dev:id/toolbarTitle"
    image_view_btn = "ru.limeshop.android.dev:id/toolbar_secondary_image_view"
    filters_btn = "ru.limeshop.android.dev:id/imageView"
    # filter_sort_title = d(resourceId="ru.limeshop.android.dev:id/item_filter_name", text="СОРТИРОВАТЬ")
    # filter_price_asc_text = d(resourceId="ru.limeshop.android.dev:id/item_checkable_option_name",
    #                           text="По возрастанию цены")
    # filter_price_desc_text = d(resourceId="ru.limeshop.android.dev:id/item_checkable_option_name",
    #                            text="По убыванию цены")
    filter_price_asc_cbox = '//*[@resource-id="ru.limeshop.android.dev:id/sorted_block"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]'
    filter_price_desc_cbox = '//*[@resource-id="ru.limeshop.android.dev:id/sorted_block"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]'
    # filter_color_title = d(resourceId="ru.limeshop.android.dev:id/item_filter_name", text="ЦВЕТ")
    color_box_1 = '//*[@resource-id="ru.limeshop.android.dev:id/filter_color_block"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]'
    color_box_2 = '//*[@resource-id="ru.limeshop.android.dev:id/filter_color_block"]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]'
    # filter_apply_btn = d(resourceId="ru.limeshop.android.dev:id/filter_apply")
    price_product_1 = '//*[@resource-id="ru.limeshop.android.dev:id/recycler_catalog"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]'
    banner_image = 'ru.limeshop.android.dev:id/media_view'
    cards_image = "ru.limeshop.android.dev:id/media_view_container_layout"
    image_card1 = '//*[@resource-id="ru.limeshop.android.dev:id/recycler_catalog"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]'
    image_card2 = '//*[@resource-id="ru.limeshop.android.dev:id/recycler_catalog"]/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]'
    SCREENFORCARDS = "ru.limeshop.android.dev:id/recycler_catalog"
    CARDPLACE = '//*[@resource-id="ru.limeshop.android.dev:id/recycler_catalog"]/android.widget.FrameLayout'
    PRICELIST = "//*[@resource-id='ru.limeshop.android.dev:id/priceTextView']"
    FAVORITEBUTTON = 'ru.limeshop.android.dev:id/favoriteImageView'
    CARDNAME = 'ru.limeshop.android.dev:id/nameTextView'
    CARDPRICE = 'ru.limeshop.android.dev:id/priceTextView'
    CHECKBOX_FILTERS = 'ru.limeshop.android.dev:id/item_checkable_option_active'


class ProductCardLocators:
    # PRODUCT_CARD
    BUY = '//*[@resource-id="ru.limeshop.android.dev:id/buy_button"]'
    BUY_MORE = '//*[@resource-id="ru.limeshop.android.dev:id/buy_more_button"]'
    COLORS = '//*[@resource-id="ru.limeshop.android.dev:id/productColorsTextView"]'
    FAVORITE = '//*[@resource-id="ru.limeshop.android.dev:id/productAddToFavoritesImageButton"]'
    SHARE = '//*[@resource-id="ru.limeshop.android.dev:id/productShareImageButton"]'
    CART = '//*[@resource-id="ru.limeshop.android.dev:id/productCartImageButton"]'
    PHOTO_ZOOM = '//*[@resource-id="ru.limeshop.android.dev:id/productPhotosViewpager"]'
    ART = 'ru.limeshop.android.dev:id/productArticleTextView'
    SIZES_GUIDE = '//*[@resource-id="ru.limeshop.android.dev:id/product_sizes_text_view"]'
    COMPOSITIONS_AND_CARE = '//*[@resource-id="ru.limeshop.android.dev:id/productCompositionAndCareTextView"]'
    DELIVERY = '//*[@resource-id="ru.limeshop.android.dev:id/productDeliveryTextView"]'
    PRODUCT_STOCKS = '//*[@resource-id="ru.limeshop.android.dev:id/productStocksTextView"]'
    PAYMENT = '//*[@resource-id="ru.limeshop.android.dev:id/productPaymentTextView"]'
    payment_url = '//*[@resource-id="com.android.browser:id/url" and contains(@text, "lime-shop.com/ru_ru/help")]'
    GOES_WELL = '//*[@resource-id="ru.limeshop.android.dev:id/goesWellTextView"]'
    YOU_LIKE_IT = '//*[@resource-id="ru.limeshop.android.dev:id/youllLikeItTextView"]'
    GOES_WELL_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/goesWellRecyclerView"]/android.widget.LinearLayout[1]'
    GOES_WELL_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/goesWellRecyclerView"]/android.widget.LinearLayout[2]'
    YOU_LIKE_IT_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/youllLikeItRecyclerView"]/android.widget.LinearLayout[1]'
    YOU_LIKE_IT_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/youllLikeItRecyclerView"]/android.widget.LinearLayout[2]'
    # BOTTOM_SHEET
    # XS_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[1]'
    # S_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[2]'
    # M_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[3]'
    # L_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[4]'
    # XL_SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[5]'
    # SIZE_34 = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[1]'
    # SIZE_36 = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[2]'
    # SIZE_38 = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[3]'
    # SIZE_40 = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[4]'
    # SIZE_42 = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[5]'
    # SIZE_44 = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[6]'
    SIZE_INFO = '//*[@resource-id="ru.limeshop.android.dev:id/sizeInfoButton"]'
    POPUP = '//*[@resource-id="ru.limeshop.android.dev:id/productPopup"]'
    POPUP_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/popupStartTitle"]'
    POPUP_BUTTON = '//*[@resource-id="ru.limeshop.android.dev:id/popupButton"]'
    # product_size_list = d(resourceId="ru.limeshop.android.dev:id/product_add_to_cart_name")
    available_size = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]//android.widget.TextView[@resource-id="ru.limeshop.android.dev:id/product_add_to_cart_name" and not(following-sibling::android.widget.TextView[@resource-id="ru.limeshop.android.dev:id/product_add_to_cart_available"])]'
    product_price = 'ru.limeshop.android.dev:id/productPriceTextView'
    product_name = 'ru.limeshop.android.dev:id/productNameTextView'
    back_btn = 'ru.limeshop.android.dev:id/closeImageButton'
    delivery_description_page = 'ru.limeshop.android.dev:id/coordinator'
    selected_color = '//*[@resource-id="ru.limeshop.android.dev:id/productColorTextView" and @selected="true"]'
    unselected_color = '//*[@resource-id="ru.limeshop.android.dev:id/productColorTextView" and @selected="false"]'
    zoom_image_back_btn = '//*[@resource-id="ru.limeshop.android.dev:id/productPhotosPager"]/following-sibling::android.widget.ImageView'
    popup_buy_btn = 'ru.limeshop.android.dev:id/productPopup'
    popup_title = 'ru.limeshop.android.dev:id/popupStartTitle'
    popup_btn = 'ru.limeshop.android.dev:id/popupButton'
    BOTTOM_SHEET = '//*[@resource-id="ru.limeshop.android.dev:id/design_bottom_sheet"]'
    SIZES_PRODUCT = 'ru.limeshop.android.dev:id/product_add_to_cart_name'
    ZOOM_VIEW = '//*[@resource-id="ru.limeshop.android.dev:id/productPhotosPager"]'


class ProfileLocators:
    # PROFILE
    PROFILE_ESTIMATION_TITLE = '//*[@text="ОЦЕНИТЕ ПРИЛОЖЕНИЕ:"]'
    PROFILE_ESTIMATION = '//android.widget.ScrollView/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[2]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.ImageView[5]'
    PRIVACY_POLICY = '// *[ @ text = "Политика конфиденциальности"]'
    TERMS_OF_PURCHASE = '// *[ @ text = "Условия покупки"]'
    FEATURE_TOGGLES = '//*[@resource-id="ru.limeshop.android.dev:id/profile_feature_toggle"]'
    VERSION_TEXT = '//*[@text="ВЕРСИЯ 3.23.6"]'
    app_id = 'ru.limeshop.android.dev:id/uuid_text_view'
    PERMISSION_SCREEN = '//*[@resource-id="com.android.permissioncontroller:id/grant_dialog"]'
    DENY_USE = '//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]'
    ONE_USE = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_one_time_button"]'
    ALLWAYS_USE = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'

    # PROFILE_UNAUTHORIZED
    MANUAL_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_manual'
    CONTACTS_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_contacts'
    COMPANY_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_company'
    SHOPS_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_shops'
    SHOP_LIST = '//*[@content-desc="Список"]'
    SHOP_MAP = '//*[@content-desc="Карта"]'
    SHOPS_PARTS_FILTERS = '//*[@resource-id="ru.limeshop.android.dev:id/collections_recycler_view"]'
    SHOPS_VIEW_LIST = 'ru.limeshop.android.dev:id/stores_list'
    SUBSCRIPTIONS_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_subscriptions'
    FEATURE_TOGGLES_UN = '//*[@resource-id="ru.limeshop.android.dev:id/profile_feature_toggle_unauthorized"]'
    CHAT_UN = '//*[@text="ЧАТ"]'
    LOGIN_AND_SIGN = '//*[@resource-id="ru.limeshop.android.dev:id/profile_registration_button"]'
    phone_number = 'ru.limeshop.android.dev:id/textView42'
    dialer_digits = '//*[@resource-id="com.android.dialer:id/digits"]'

    # PROFILE_AUTHORIZED
    USERNAME = 'ru.limeshop.android.dev:id/nameTextView'
    EMAIL = 'ru.limeshop.android.dev:id/emailTextView'
    ORDERS = 'ru.limeshop.android.dev:id/profile_authorized_orders'
    MY_INFO = 'ru.limeshop.android.dev:id/profile_authorized_my_info'
    MANUAL = 'ru.limeshop.android.dev:id/profile_authorized_manual'
    CONTACTS = 'ru.limeshop.android.dev:id/profile_authorized_contacts'
    COMPANY = 'ru.limeshop.android.dev:id/profile_authorized_company'
    SHOPS = 'ru.limeshop.android.dev:id/profile_authorized_shops'
    SUBSCRIPTIONS = 'ru.limeshop.android.dev:id/profile_authorized_subscriptions'
    LOGOUT = 'ru.limeshop.android.dev:id/profile_authorized_logout'
    DELETE_ACCOUNT = 'ru.limeshop.android.dev:id/deleteAccountTextView'
    add_new_address_btn = 'ru.limeshop.android.dev:id/my_info_new_address'
    city = '//*[@resource-id="ru.limeshop.android.dev:id/info_city"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    street = '//*[@resource-id="ru.limeshop.android.dev:id/info_street"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    apartment = '//*[@resource-id="ru.limeshop.android.dev:id/info_apartment"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    postcode = '//*[@resource-id="ru.limeshop.android.dev:id/info_postcode"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    address_popup = 'ru.limeshop.android.dev:id/popUpRecycler'
    save_address_btn = 'ru.limeshop.android.dev:id/save_address_button'

    # SUBSCRIBED_ELEMENTS
    SUBSCRIPTIONS_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/toolbarTitle"]'
    SUBSCRIPTIONS_BTN_BACK = '//android.widget.ImageButton'
    SUBSCRIPTIONS_PUSH = '//*[@resource-id="ru.limeshop.android.dev:id/pushTitle"]'
    SUBSCRIPTIONS_PUSH_SWITCH = '//*[@resource-id="ru.limeshop.android.dev:id/pushSwitch"]'
    SUBSCRIPTIONS_MAIL = '//*[@resource-id="ru.limeshop.android.dev:id/mailTitle"]'
    SUBSCRIPTIONS_MAIL_SWITCH = '//*[@resource-id="ru.limeshop.android.dev:id/emailSwitch"]'
    SUBSCRIPTIONS_WOMEN = '//*[@text="Женщины"]'
    SUBSCRIPTIONS_WOMEN_CHBX = '//*[@resource-id="ru.limeshop.android.dev:id/subscribe_kinds_recycler_view"]/android.widget.LinearLayout[1]/android.widget.ImageView[1]'
    SUBSCRIPTIONS_MEN = '//*[@text="Мужчины"]'
    SUBSCRIPTIONS_MEN_CHBX = '//*[@resource-id="ru.limeshop.android.dev:id/subscribe_kinds_recycler_view"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]'
    SUBSCRIPTIONS_KIDS = '//*[@text="Дети"]'
    SUBSCRIPTIONS_KIDS_CHBX = '//*[@resource-id="ru.limeshop.android.dev:id/subscribe_kinds_recycler_view"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]'
    SUBSCRIPTIONS_BTN_SAVE = '//*[@resource-id="ru.limeshop.android.dev:id/subscribe_button"]'

    #TERMS_OF_PURCHASE
    OFFER_DOCUMENT = '//*[@resource-id="ru.limeshop.android.dev:id/baseContainer"]'
    BTN_BACK_TERMS = "//android.widget.ImageButton"
    PRIVACY_POLICY_DOCUMENT = '//*[@resource-id="ru.limeshop.android.dev:id/baseContainer"]'
    PRIVACY_POLICY_BTN_BACK = '//android.widget.ImageButton'

class FeatureTogglesLocators:
    SWITCH_1 = '//*[@resource-id="ru.limeshop.android.dev:id/toggleRecycler"]/android.view.ViewGroup[1]/android.widget.Switch[1]'
    SWITCH_2 = '//*[@resource-id="ru.limeshop.android.dev:id/toggleRecycler"]/android.view.ViewGroup[2]/android.widget.Switch[1]'
    SWITCH_3 = '//*[@resource-id="ru.limeshop.android.dev:id/toggleRecycler"]/android.view.ViewGroup[3]/android.widget.Switch[1]'
    SWITCH_4 = '//*[@resource-id="ru.limeshop.android.dev:id/toggleRecycler"]/android.view.ViewGroup[4]/android.widget.Switch[1]'
    SWITCH_5 = '//*[@resource-id="ru.limeshop.android.dev:id/toggleRecycler"]/android.view.ViewGroup[5]/android.widget.Switch[1]'


class LoginLocators:
    title_text = "ru.limeshop.android.dev:id/title_text"
    subtitle_text = "ru.limeshop.android.dev:id/subtitle_text"
    label_text = "ru.limeshop.android.dev:id/labelText"
    phone_field = "ru.limeshop.android.dev:id/editText"
    get_code_button = "ru.limeshop.android.dev:id/get_code_button"
    privacy_policy_text = "ru.limeshop.android.dev:id/privacy_policy_text"
    errorText = "ru.limeshop.android.dev:id/errorText"
    number_text_1 = '//*[@resource-id="ru.limeshop.android.dev:id/first_number_layout"]/android.widget.EditText[1]'
    number_text_2 = '//*[@resource-id="ru.limeshop.android.dev:id/second_number_layout"]/android.widget.EditText[1]'
    number_text_3 = '//*[@resource-id="ru.limeshop.android.dev:id/third_number_layout"]/android.widget.EditText[1]'
    number_text_4 = '//*[@resource-id="ru.limeshop.android.dev:id/fourth_number_layout"]/android.widget.EditText[1]'

    # LOGIN_SCREEN
    LOGIN_SCREEN_TITLE = 'ru.limeshop.android.dev:id/orderflow_signin_title'
    # LOGIN_SCREEN_HINT_EMAIL = d(resourceId="ru.limeshop.android.dev:id/hintText", text="Эл. почта")
    LOGIN_SCREEN_EMAIL = '//*[@resource-id="ru.limeshop.android.dev:id/signin_email"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    # LOGIN_SCREEN_HINT_PASS = d(resourceId="ru.limeshop.android.dev:id/hintText", text="Пароль")
    LOGIN_SCREEN_PASS = '//*[@resource-id="ru.limeshop.android.dev:id/signin_password"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    LOGIN_SCREEN_SHOW_PASS = 'ru.limeshop.android.dev:id/endIcon'
    LOGIN_SCREEN_PASS_RESET = 'ru.limeshop.android.dev:id/signin_password_reset'
    LOGIN_SCREEN_SIGNIN = 'ru.limeshop.android.dev:id/signin_proceed'
    PASSWORD_RESET_LINK = "ru.limeshop.android.dev:id/signin_password_reset"
    LOGIN_BTN = "ru.limeshop.android.dev:id/signin_proceed"
    SIGN_UP_BTN = "ru.limeshop.android.dev:id/signUpButton"

    # REG_SCREEN
    SIGNUP_HINT_NAME = '"ru.limeshop.android.dev:id/hintText", text="Имя"'
    SIGNUP_NAME = '//*[@resource-id="ru.limeshop.android.dev:id/signup_name"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    SIGNUP_HINT_SURNAME = '"ru.limeshop.android.dev:id/hintText", text="Фамилия"'
    SIGNUP_SURNAME = '//*[@resource-id="ru.limeshop.android.dev:id/signup_lastname"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    SIGNUP_PHONE = '//*[@resource-id="ru.limeshop.android.dev:id/signup_phone"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    SIGNUP_HINT_PHONE = '"ru.limeshop.android.dev:id/hintText", text="Моб. телефон"'
    SIGNUP_EMAIL = '//*[@resource-id="ru.limeshop.android.dev:id/signup_email"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    SIGNUP_HINT_EMAIL = 'ru.limeshop.android.dev:id/hintText, text="Эл. почта"'
    SIGNUP_PASSWORD = '//*[@resource-id="ru.limeshop.android.dev:id/signup_password"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    SIGNUP_HINT_PASSWORD = '"ru.limeshop.android.dev:id/hintText", text="Пароль"'
    SIGNUP_REPEAT_PASSWORD = '//*[@resource-id="ru.limeshop.android.dev:id/signup_password_confirm"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    SIGNUP_HINT_REPEAT_PASSWORD = '"ru.limeshop.android.dev:id/hintText", text="Повтор нового пароля"'
    SIGNUP_SHOW_PASSWORD = '//*[@resource-id="ru.limeshop.android.dev:id/signup_password"]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
    SIGNUP_SHOW_REPEAT_PASSWORD = '//*[@resource-id="ru.limeshop.android.dev:id/signup_password_confirm"]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
    SIGNUP_SUBSCRIBE_TITLE = '//*[@text="Подписаться на новостную рассылку:"]'
    SIGNUP_SUBSCRIBE_WOMEN = '//*[@resource-id="ru.limeshop.android.dev:id/subscriptionRecycler"]/android.widget.LinearLayout[1]/android.widget.ImageView[1]'
    SIGNUP_SUBSCRIBE_MEN = '//*[@resource-id="ru.limeshop.android.dev:id/subscriptionRecycler"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]'
    SIGNUP_SUBSCRIBE_KIDS = '//*[@resource-id="ru.limeshop.android.dev:id/subscriptionRecycler"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]'
    SIGNUP_SUBSCRIBE_WOMEN_LABEL = '"ru.limeshop.android.dev:id/item_checkable_option_name", text="Женщины"'
    SIGNUP_SUBSCRIBE_MEN_LABEL = '"ru.limeshop.android.dev:id/item_checkable_option_name", text="Мужчины"'
    SIGNUP_SUBSCRIBE_KIDS_LABEL = '"ru.limeshop.android.dev:id/item_checkable_option_name", text="Дети"'
    SIGNUP_TERMS_TEXT = "ru.limeshop.android.dev:id/signup_terms_text_view"
    SIGNUP_SUBSCRIBE_ACCEPT = '//*[@resource-id="ru.limeshop.android.dev:id/checkable_option_active"]'
    SIGNUP_RESUME_BTN = '//*[@text="ПРОДОЛЖИТЬ"]'
    profile_avatar = 'ru.limeshop.android.dev:id/avatarImageView'


class CartLocators:
    CLEAR_ALL = 'ru.limeshop.android.dev:id/toolbar_secondary_text_view'
    FAVORITE = '//*[@resource-id="ru.limeshop.android.dev:id/favorites_image_view"]'
    PRODUCT_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_name"]'
    TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/toolbarTitle"]'
    ART = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_code"]'
    SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_size"]'
    COLOR = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_color"]'
    PRICE_TOTAL = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_total_price"]'
    PRICE_SALE = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_price_sale"]'
    DELETE = '//*[@resource-id="ru.limeshop.android.dev:id/delete_image_view"]'
    MINUS = '//*[@resource-id="ru.limeshop.android.dev:id/minus_image_view"]'
    PLUS = '//*[@resource-id="ru.limeshop.android.dev:id/plus_image_view"]'
    QUANTITY = '//*[@resource-id="ru.limeshop.android.dev:id/quantity_text_view"]'
    QUANTITY_TEXT = '//*[@resource-id="ru.limeshop.android.dev:id/textView3"]'
    PROMO_CODE = '//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    PRICE_TEXT = '//*[@resource-id="ru.limeshop.android.dev:id/textView5"]'
    SUMMARY_QUANTITY = '//*[@resource-id="ru.limeshop.android.dev:id/textView2"]'
    SUMMARY_PRICE = '//*[@resource-id="ru.limeshop.android.dev:id/textView4"]'
    SUMMARY_TEXT = '//*[@resource-id="ru.limeshop.android.dev:id/textView11"]'
    FINAL_PRICE = "ru.limeshop.android.dev:id/textView10"
    DISCOUNT = "ru.limeshop.android.dev:id/textView6"
    CONTINUE = '//*[@resource-id="ru.limeshop.android.dev:id/cart_continue_button"]'
    gift_card_error = 'ru.limeshop.android.dev:id/errorText'
    # CLEAR CART
    ICON = '//androidx.appcompat.widget.LinearLayoutCompat/android.widget.ImageView[1]'
    DESCRIPTION_CLEAR = '//*[@text="ВАША КОРЗИНА ПУСТА"]'
    BUY_BUTTON = '//*[@resource-id="ru.limeshop.android.dev:id/cart_buy_button"]'
    # POPUP
    POPUP_CLEAR = '//*[@resource-id="ru.limeshop.android.dev:id/positive_button_outlined"]'
    POPUP_CANCEL = '//*[@resource-id="ru.limeshop.android.dev:id/negative_button"]'
    POPUP_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/title_text_view"]'
    POPUP_DESCRIPTION = '//*[@resource-id="ru.limeshop.android.dev:id/message_text_view"]'
    #
    card_photo = 'ru.limeshop.android.dev:id/item_cart_photo'
    email_field = '//*[@text="Эл. почта"]'
    password_field = '//*[@text="Пароль"]'
    sign_in_btn = 'ru.limeshop.android.dev:id/signin_proceed'
    register_btn = '//*[@resource-id="ru.limeshop.android.dev:id/signUpButton"]'


class CheckOutLocators:
    DELIVERY_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_title_text"]'
    DELIVERY_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]'
    DELIVERY_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]'
    DELIVERY_SELECTOR_3 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[3]/android.widget.FrameLayout[1]'
    DELIVERY_TEXT_CUR = '//*[@text="КУРЬЕРОМ"]'
    DELIVERY_TEXT_SELF = '//*[@text="САМОВЫВОЗ"]'
    DELIVERY_PRICE_1 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]'
    DELIVERY_PRICE_2 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.TextView[2]'
    ADDRESS = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_info_title_text"]'
    SELECTED_ADDRESS = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_courier_title_text"]'
    ADD_ADDRESS_BUTTON = '//*[@resource-id="ru.limeshop.android.dev:id/add_courier_address_button"]'
    EDIT_ADDRESS = '//*[@resource-id="ru.limeshop.android.dev:id/edit_courier_address_image"]'
    NAME = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_info_subtitle_text"]'
    PAYMENT_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/payment_title_text"]'
    PAYMENT_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/payment_selector_component"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]'
    PAYMENT_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/payment_selector_component"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]'
    PAYMENT_SELECTOR_3 = '//*[@resource-id="ru.limeshop.android.dev:id/payment_selector_component"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[3]/android.widget.FrameLayout[1]'
    PAYMENT_SELECTOR_4 = '//*[@resource-id="ru.limeshop.android.dev:id/payment_selector_component"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[4]/android.widget.FrameLayout[1]'
    PAYMENT_TITLE_1 = '//*[@text="ЧЕРЕЗ СБП"]'
    PAYMENT_TITLE_2 = '//*[@text="КАРТОЙ ОНЛАЙН"]'
    PAYMENT_TITLE_3 = '//*[@text="ПОДАРОЧНОЙ КАРТОЙ"]'
    PAYMENT_TITLE_4 = '//*[@text="ПРИ ПОЛУЧЕНИИ"]'
    PAYMENT_INFO_TEXT = '//*[@resource-id="ru.limeshop.android.dev:id/cash_title_text"]'
    SLOTS_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/time_slots_title_text"]'
    SLOTS_DATE_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/date_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]'
    SLOTS_DATE_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/date_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]'
    SLOTS_DATE_SELECTOR_3 = '//*[@resource-id="ru.limeshop.android.dev:id/date_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]'
    SLOTS_TIME_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/time_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]'
    SLOTS_TIME_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/time_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]'
    SLOTS_TIME_SELECTOR_3 = '//*[@resource-id="ru.limeshop.android.dev:id/time_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[3]'
    SLOTS_TIME_SELECTOR_4 = '//*[@resource-id="ru.limeshop.android.dev:id/time_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[4]'
    ORDER_LIST_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/order_list_title_text"]'
    ORDER_LIST_SHEVRON = '//*[@resource-id="ru.limeshop.android.dev:id/order_list_chevron_image"]'
    SUMMARY_QUANTITY_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_quantity_title_text"]'
    SUMMARY_QUANTITY = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_quantity_text"]'
    SUMMARY_COAST_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_cost_title_text"]'
    SUMMARY_COAST = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_cost_text"]'
    SUMMARY_TOTAL_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_total_title_text"]'
    SUMMARY_TOTAL = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_total_text"]'
    summary_discount = "ru.limeshop.android.dev:id/checkout_summary_discount_text"
    ORDER_PAY = '//*[@resource-id="ru.limeshop.android.dev:id/order_pay_button"]'
    TERMS_TEXT = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_terms_text"]'
    POPUP_BACK_CART_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/title_text_view"]'
    POPUP_BACK_CART_DESCRIPTION = '//*[@resource-id="ru.limeshop.android.dev:id/message_text_view"]'
    POPUP_BACK_CART_CANCEL = '//*[@resource-id="ru.limeshop.android.dev:id/positive_button"]'
    POPUP_BACK_CART_YES = '//*[@resource-id="ru.limeshop.android.dev:id/negative_button"]'
    ADD_NEW_CARD_PLUS = 'ru.limeshop.android.dev:id/add_payment_button'
    # Card online
    CARD_ICON = '//*[@resource-id="ru.limeshop.android.dev:id/payment_card_image"]'
    CARD_INFO = '//*[@resource-id="ru.limeshop.android.dev:id/payment_card_number_text"]'
    CARD_EDIT = '//*[@resource-id="ru.limeshop.android.dev:id/edit_payment_card_image"]'
    # BOTTOM-SHEET YOUR CARDS
    CARD_LIST_TITLE = '//*[@text="ВАШИ КАРТЫ"]'
    CARD_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/is_selected_card_radio"]'
    CARD_ICON_BOTTOM_SHEET = '//*[@resource-id="ru.limeshop.android.dev:id/icon_image_view"]'
    CARD_INFO_BOTTOM_SHEET = '//*[@resource-id="ru.limeshop.android.dev:id/info_text_view"]'
    CARD_DELETE_SOLO = '//*[@resource-id="ru.limeshop.android.dev:id/delete_image_view"]'
    CARD_DELETE_1 = '//*[@resource-id="ru.limeshop.android.dev:id/saved_cards_recycler_view"]/android.view.ViewGroup[1]/android.widget.ImageView[2]'
    CARD_DELETE_2 = '//*[@resource-id="ru.limeshop.android.dev:id/saved_cards_recycler_view"]/android.view.ViewGroup[2]/android.widget.ImageView[2]'
    ADD_NEW_CARD_BUTTON = '//*[@resource-id="ru.limeshop.android.dev:id/add_new_card_button"]'
    # BOTTOM-SHEET ADD CARD
    ADD_CARD_TITLE = '//*[@text="ДОБАВИТЬ КАРТУ"]'
    ADD_CARD_NUMBER = '//*[@resource-id="ru.limeshop.android.dev:id/card_number"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    ADD_CARD_OWNER = '//*[@resource-id="ru.limeshop.android.dev:id/card_owner"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    ADD_CARD_EXPIRY = '//*[@resource-id="ru.limeshop.android.dev:id/card_expiry"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    ADD_CARD_CVV = '//*[@resource-id="ru.limeshop.android.dev:id/card_security"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    ADD_CARD_SAVE_CHECK_BOX = '//*[@resource-id="ru.limeshop.android.dev:id/saveCardCheckBox"]'
    ADD_CARD_SAVE_BUTTON = '//*[@resource-id="ru.limeshop.android.dev:id/order_continue_button"]'
    # POP-UP DELETE CARD
    DEL_CARD_POP_UP_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/title_text_view"]'
    DEL_CARD_POP_UP_DESCRIPTION = '//*[@resource-id="ru.limeshop.android.dev:id/message_text_view"]'
    DEL_CARD_POP_UP_DELETE = '//*[@resource-id="ru.limeshop.android.dev:id/danger_button"]'
    DEL_CARD_POP_UP_CANCEL = '//*[@resource-id="ru.limeshop.android.dev:id/negative_button"]'
    # ADD ADDRESS BOTTOM-SHEET
    ADD_ADDRESS_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/title_text"]'
    ADD_ADDRESS_CITY = '//*[@resource-id="ru.limeshop.android.dev:id/edit_city"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    ADD_ADDRESS_POPUP = '//*[@resource-id="ru.limeshop.android.dev:id/popupTextView"]'
    ADD_ADDRESS_STREET = '//*[@resource-id="ru.limeshop.android.dev:id/edit_street"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    ADD_ADDRESS_APARTMENT = '//*[@resource-id="ru.limeshop.android.dev:id/edit_apartment"]/android.view.ViewGroup[1]/android.widget.EditText[1]'
    ADD_ADDRESS_SAVE_BUTTON = '//*[@text="СОХРАНИТЬ"]'
    # ADD surcharge
    SURCHARGE_SBP_SELECTOR = '//*[@resource-id="ru.limeshop.android.dev:id/saved_cards_recycler_view"]/android.view.ViewGroup[1]/android.widget.RadioButton[1]'
    # SBP SCREEN
    SBP_BANK_LIST_TITLE = "ru.limeshop.android.dev:id/banks_title_text"
    SBP_BANK_LIST_SEARCH_FIELD = "ru.limeshop.android.dev:id/editText"
    SBP_SELECTOR_TINKOFF = '//*[@resource-id="ru.limeshop.android.dev:id/info_text" and @text="Тинькофф Банк"]'
    STATUS_PAY_TITLE = "ru.limeshop.android.dev:id/status_title_text"
    #
    date = '//*[@resource-id="ru.limeshop.android.dev:id/date_selector_view"]//*[@resource-id="ru.limeshop.android.dev:id/text_container_layout"]'
    time = '//*[@resource-id="ru.limeshop.android.dev:id/time_selector_view"]//*[@resource-id="ru.limeshop.android.dev:id/selector_card"]'
    # add_gift_card_title = d(resourceId="ru.limeshop.android.dev:id/title_view", text="ДОБАВИТЬ ПОДАРОЧНУЮ КАРТУ")
    gift_card_number_field = '//*[@resource-id="ru.limeshop.android.dev:id/number_text_input_edit"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    gift_card_sum_field = '//*[@resource-id="ru.limeshop.android.dev:id/amount_text_input_edit"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    gift_card_pin_field = '//*[@resource-id="ru.limeshop.android.dev:id/pin_text_input_edit"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    gift_card_balance = 'ru.limeshop.android.dev:id/errorText'
    gift_card_continue_btn = '//*[@text="ПРОДОЛЖИТЬ"]'
    pickup_selector = '//*[@text="САМОВЫВОЗ"]/..'
    courier_selector = '//*[@text="КУРЬЕРОМ"]/..'
    card_online_selector = '//*[@text="КАРТОЙ ОНЛАЙН"]/..'
    sbp_selector = '//*[@text="ЧЕРЕЗ СБП"]/..'
    gift_card_selector = '//*[@text="ПОДАРОЧНОЙ КАРТОЙ"]/..'
    receiving_selector = '//*[@text="ПРИ ПОЛУЧЕНИИ"]/..'
    # upon_receipt_text = d(resourceId="ru.limeshop.android.dev:id/payment_info_title_text",
    #                       text='НАЛИЧНЫМИ ИЛИ КАРТОЙ ПРИ ПОЛУЧЕНИИ')
    permission_while_using_the_app = 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'
    gift_number_text = '//*[@resource-id="ru.limeshop.android.dev:id/payment_gift_number_text"]'
    gift_card_dragger_view = 'ru.limeshop.android.dev:id/dragger_view'
    add_payment_btn = 'ru.limeshop.android.dev:id/add_payment_button'
    add_gift_card_btn = 'ru.limeshop.android.dev:id/add_payment_gift_button'
    gift_card_error = 'ru.limeshop.android.dev:id/errorText'
    payment_add_card_btn = 'ru.limeshop.android.dev:id/payment_add_card_text'
    payment_add_card_selector = 'ru.limeshop.android.dev:id/is_selected_card_radio'
    card_number = '//*[@resource-id="ru.limeshop.android.dev:id/card_number"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    cardholder = '//*[@resource-id="ru.limeshop.android.dev:id/card_owner"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    card_date = '//*[@resource-id="ru.limeshop.android.dev:id/card_expiry"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    card_cvv = '//*[@resource-id="ru.limeshop.android.dev:id/card_security"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    save_card_btn = 'ru.limeshop.android.dev:id/order_continue_button'
    cloud_payments = 'com.android.systemui:id/navigation_bar_frame'
    add_courier_address_btn = 'ru.limeshop.android.dev:id/add_courier_address_button'
    city = '//*[@resource-id="ru.limeshop.android.dev:id/edit_city"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    street = '//*[@resource-id="ru.limeshop.android.dev:id/edit_street"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    apartment = '//*[@resource-id="ru.limeshop.android.dev:id/edit_apartment"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    postcode = '//*[@resource-id="ru.limeshop.android.dev:id/edit_postcode"]//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    address_popup = 'ru.limeshop.android.dev:id/popUpRecycler'
    save_address_btn = '//*[@text="СОХРАНИТЬ"]'
    order_list_price_with_sale = "ru.limeshop.android.dev:id/sale_text"


class RepeatPayLocators:
    repeat_pay_btn = "ru.limeshop.android.dev:id/action_button"
    order = "ru.limeshop.android.dev:id/orders_recycler"


class SuccessPayScreenLocators:
    ICON = '//*[@resource-id="ru.limeshop.android.dev:id/status_icon_image"]'
    TITLE = 'ru.limeshop.android.dev:id/status_title_text'
    DESCRIPTION = '//*[@text="Отслеживать его статус вы можете в личном кабинете"]'
    DESCRIPTION_FAIL = '//*[@text="Мы сохранили ваш заказ в личном кабинете — оплатите его в течение 8 минут"]'
    BUTTON = 'ru.limeshop.android.dev:id/action_button'


class PermissionGeoLocators:
    title = "com.android.permissioncontroller:id/permission_message"
    allow_foreground_only_button = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    allow_one_time_button = "com.android.permissioncontroller:id/permission_allow_one_time_button"
    deny_button = "com.android.permissioncontroller:id/permission_deny_button"
    img_1 = "com.android.permissioncontroller:id/permission_location_accuracy_radio_fine"
    img_2 = "com.android.permissioncontroller:id/permission_location_accuracy_radio_coarse"


class PickupLocators:
    tab_map = "ru.limeshop.android.dev:id/maps_title_text"
    tab_list = "ru.limeshop.android.dev:id/list_title_text"
    search_field = "ru.limeshop.android.dev:id/editText"
    filter_lime = '//*[@resource-id="ru.limeshop.android.dev:id/selector_recycler_view"]/android.widget.FrameLayout[1]'
    filter_boxberry = '//*[@resource-id="ru.limeshop.android.dev:id/selector_recycler_view"]/android.widget.FrameLayout[2]'
    filter_yandex = '//*[@resource-id="ru.limeshop.android.dev:id/selector_recycler_view"]/android.widget.FrameLayout[3]'
    list_select_1 = '//*[@resource-id="ru.limeshop.android.dev:id/pickup_points_recycler"]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.RelativeLayout[2]/android.widget.Button[1]'
    list_select_2 = '//*[@resource-id="ru.limeshop.android.dev:id/pickup_points_recycler"]/androidx.appcompat.widget.LinearLayoutCompat[2]/android.widget.RelativeLayout[2]/android.widget.Button[1]'
    list_select_3 = '//*[@resource-id="ru.limeshop.android.dev:id/pickup_points_recycler"]/androidx.appcompat.widget.LinearLayoutCompat[3]/android.widget.RelativeLayout[2]/android.widget.Button[1]'
    info_btn_1 = '//*[@resource-id="ru.limeshop.android.dev:id/pickup_points_recycler"]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]'
    info_btn_2 = '//*[@resource-id="ru.limeshop.android.dev:id/pickup_points_recycler"]/androidx.appcompat.widget.LinearLayoutCompat[2]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]'
    info_btn_3 = '//*[@resource-id="ru.limeshop.android.dev:id/pickup_points_recycler"]/androidx.appcompat.widget.LinearLayoutCompat[3]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]'
    # INFO SCREEN
    info_name_text = "ru.limeshop.android.dev:id/pickup_point_info_name_text"
    info_address_text = "ru.limeshop.android.dev:id/pickup_point_info_address_text"
    info_schedule_text = "ru.limeshop.android.dev:id/pickup_point_info_schedule_text"
    title_address = '//*[@text="АДРЕС"]'
    title_schedule = '//*[@text="ВРЕМЯ РАБОТЫ"]'
    take_point_btn = '//*[@text="ЗАБЕРУ ОТСЮДА"]'
    order_here_button = "ru.limeshop.android.dev:id/order_here_button"


class FavoritesLocators:
    BUTTONBACK = "//android.widget.ImageButton"
    TITLE = 'ru.limeshop.android.dev:id/toolbarTitle'
    BUTTONBUY = 'ru.limeshop.android.dev:id/buyButton'
    INFOTEXT = '//*[@text="ВАШ ВИШЛИСТ ПУСТ"]'
    BUTTONFAVORITES = '//*[@resource-id="ru.limeshop.android.dev:id/favoritesRecyclerView"]/android.view.ViewGroup[1]/android.widget.ImageView[1]'
    BUTTONFAVORITES2 = '//*[@resource-id="ru.limeshop.android.dev:id/favoritesRecyclerView"]/android.view.ViewGroup[2]/android.widget.ImageView[1]'
    STUFF = '//*[@resource-id="ru.limeshop.android.dev:id/favoritesRecyclerView"]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]'
    STUFFNAME = '//*[@resource-id="ru.limeshop.android.dev:id/item_product_name"]'
    STUFFPRICE = '//*[@resource-id="ru.limeshop.android.dev:id/item_product_price"]'
    BUTTONBUYSTUFF = '//*[@resource-id="ru.limeshop.android.dev:id/favoritesRecyclerView"]/android.view.ViewGroup[1]/android.widget.Button[1]'
    MODULEWINDOW = '//*[@resource-id="ru.limeshop.android.dev:id/design_bottom_sheet"]/android.widget.LinearLayout[1]'
    SIZEINSTUCTION = "ru.limeshop.android.dev:id/sizeInfoButton"
    SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/sizeList"]/android.view.ViewGroup[1]'
    SNECKBARADDCART = "ru.limeshop.android.dev:id/favoritePopup"
    SNECKBARBUTTONGOTOCART = "ru.limeshop.android.dev:id/popupButton"
    card_name = '//*[@resource-id="ru.limeshop.android.dev:id/item_product_name"]'
    SWIPEBUTTON = "ru.limeshop.android.dev:id/view5"
    SCREENFORCARDS = "ru.limeshop.android.dev:id/baseContainer"
    EVENCARD = 'ru.limeshop.android.dev:id/favoritesRecyclerView"]/android.view.ViewGroup[2]'
    ODDCARD = 'ru.limeshop.android.dev:id/favoritesRecyclerView"]/android.view.ViewGroup[3]'
    cards_list = '//*[@resource-id="ru.limeshop.android.dev:id/favoritesRecyclerView"]/android.view.ViewGroup'
    BOTTONDELETEFROMFAV = '//*[@resource-id="ru.limeshop.android.dev:id/removeImageView"]'
