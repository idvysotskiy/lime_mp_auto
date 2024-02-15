# file: locators.py
class MainLocators:
    # BASE
    X_BUTTON = '//android.widget.ImageButton'
    NOTIFICATION_NEGATIVE = '//*[@resource-id="ru.limeshop.android.dev:id/notification_negative_button"]'
    TOOLBAR_TITLE = 'ru.limeshop.android.dev:id/toolbarTitle'

    # NAV_BAR
    SEARCH_NAV = 'ru.limeshop.android.dev:id/nav_search'
    FAVORITES_NAV = 'ru.limeshop.android.dev:id/nav_favorites'
    CATALOG_NAV = '//*[@resource-id="ru.limeshop.android.dev:id/nav_catalog_menu"]/android.widget.FrameLayout[1]'
    PROFILE_NAV = 'ru.limeshop.android.dev:id/nav_profile'
    CART_NAV = 'ru.limeshop.android.dev:id/nav_cart'

    # CATALOG
    CATALOG_ITEM = 'ru.limeshop.android.dev:id/catalog_item_name'
    FAV_ICON = 'ru.limeshop.android.dev:id/favoriteImageView'
    NAME_PRODUCT_COLLECTION = 'ru.limeshop.android.dev:id/nameTextView'
    NAME_PRODUCT_FAVORITE = 'ru.limeshop.android.dev:id/item_product_name'
    FILTER_BUTTON = '//*[@resource-id="ru.limeshop.android.dev:id/filter_menu"]'
    PRODUCT_CARD_1_1 = '//android.widget.TableLayout/android.widget.TableRow[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]'
    PRODUCT_CARD_2_2 = '//android.widget.TableLayout/android.widget.TableRow[2]/android.view.ViewGroup[2]/android.widget.FrameLayout[1]'


class ProductCard:
    # PRODUCT_CARD
    BUY = '//*[@resource-id="ru.limeshop.android.dev:id/buy_button"]'
    COLORS = '//*[@resource-id="ru.limeshop.android.dev:id/productColorsConstraintLayout"]'
    FAVORITE = '//*[@resource-id="ru.limeshop.android.dev:id/productAddToFavoritesImageButton"]'
    SHARE = '//*[@resource-id="ru.limeshop.android.dev:id/productShareImageButton"]'
    CART = '//*[@resource-id="ru.limeshop.android.dev:id/productCartImageButton"]'
    PHOTO_ZOOM = '//*[@resource-id="ru.limeshop.android.dev:id/productPhotosViewpager"]'
    ART = '//*[@resource-id="ru.limeshop.android.dev:id/productArticleTextView"]'
    SIZES_GUIDE = '//*[@resource-id="ru.limeshop.android.dev:id/product_sizes_text_view"]'
    COMPOSITIONS_AND_CARE = '//*[@resource-id="ru.limeshop.android.dev:id/productCompositionAndCareTextView"]'
    DELIVERY = '//*[@resource-id="ru.limeshop.android.dev:id/productDeliveryTextView"]'
    PAYMENT = '//*[@resource-id="ru.limeshop.android.dev:id/productPaymentTextView"]'
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


class Profile:
    # PROFILE
    PROFILE_ESTIMATION_TITLE = '//*[@text="ОЦЕНИТЕ ПРИЛОЖЕНИЕ:"]'
    PROFILE_ESTIMATION = '//android.widget.ScrollView/android.widget.LinearLayout[1]/androidx.appcompat.widget.LinearLayoutCompat[2]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.ImageView[5]'
    PRIVACY_POLICY = '// *[ @ text = "Политика конфиденциальности"]'
    TERMS_OF_PURCHASE = '// *[ @ text = "Условия покупки"]'
    FEATURE_TOGGLES = '//*[@resource-id="ru.limeshop.android.dev:id/profile_feature_toggle"]'
    VERSION_TEXT = '//*[@text="ВЕРСИЯ 3.23.6"]'

    # PROFILE_UNAUTHORIZED
    MANUAL_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_manual'
    CONTACTS_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_contacts'
    COMPANY_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_company'
    SHOPS_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_shops'
    SUBSCRIPTIONS_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_subscriptions'
    FEATURE_TOGGLES_UN = '//*[@resource-id="ru.limeshop.android.dev:id/profile_feature_toggle_unauthorized"]'
    CHAT_UN = '//*[@text="ЧАТ"]'
    LOGIN_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_login'
    SIGNUP_UN = 'ru.limeshop.android.dev:id/profile_unauthorized_signup'

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

class FeatureToggles:
    SWITCH_1 = '//*[@resource-id="ru.limeshop.android.dev:id/toggleRecycler"]/android.view.ViewGroup[1]/android.widget.Switch[1]'
    SWITCH_2 = '//*[@resource-id="ru.limeshop.android.dev:id/toggleRecycler"]/android.view.ViewGroup[2]/android.widget.Switch[1]'
    SWITCH_3 = '//*[@resource-id="ru.limeshop.android.dev:id/toggleRecycler"]/android.view.ViewGroup[3]/android.widget.Switch[1]'
class LoginLocators:
    # LOGIN_SCREEN
    LOGIN_SCREEN_TITLE = 'ru.limeshop.android.dev:id/orderflow_signin_title'
    LOGIN_SCREEN_HINT_EMAIL = 'ru.limeshop.android.dev:id/hintText, text="Эл. почта"'
    LOGIN_SCREEN_EMAIL = 'ru.limeshop.android.dev:id/signin_email'
    LOGIN_SCREEN_HINT_PASS = '"ru.limeshop.android.dev:id/hintText", text="Пароль"'
    LOGIN_SCREEN_PASS = 'ru.limeshop.android.dev:id/signin_password'
    LOGIN_SCREEN_SHOW_PASS = 'ru.limeshop.android.dev:id/endIcon'
    LOGIN_SCREEN_PASS_RESET = 'ru.limeshop.android.dev:id/signin_password_reset'
    LOGIN_SCREEN_SIGNIN = 'ru.limeshop.android.dev:id/signin_proceed'

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


class Cart:
    CLEAR_ALL = '//*[@resource-id="ru.limeshop.android.dev:id/toolbar_secondary_text_view"]'
    FAVORITE = '//*[@resource-id="ru.limeshop.android.dev:id/favorites_image_view"]'
    PRODUCT_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_name"]'
    ART = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_code"]'
    SIZE = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_size"]'
    COLOR = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_color"]'
    PRICE_TOTAL = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_total_price"]'
    PRICE_SALE = '//*[@resource-id="ru.limeshop.android.dev:id/item_cart_price_sale"]'
    DELETE = '//*[@resource-id="ru.limeshop.android.dev:id/delete_image_view"]'
    MINUS = '//*[@resource-id="ru.limeshop.android.dev:id/minus_image_view"]'
    PLUS = '//*[@resource-id="ru.limeshop.android.dev:id/plus_image_view"]'
    QUANTITY = '//*[@resource-id="ru.limeshop.android.dev:id/quantity_text_view"]'
    PROMO_CODE = '//*[@resource-id="ru.limeshop.android.dev:id/editText"]'
    SUMMARY_QUANTITY = '//*[@resource-id="ru.limeshop.android.dev:id/textView2"]'
    SUMMARY_PRICE = '//*[@resource-id="ru.limeshop.android.dev:id/textView4"]'
   # SUMMARY_PRICE_FINAL =

class CheckOut:
    DELIVERY_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_title_text"]'
    DELIVERY_SELECTOR_1 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]'
    DELIVERY_SELECTOR_2 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[1]'
    DELIVERY_CUR = '//*[@text="КУРЬЕРОМ"]'
    DELIVERY_SELF = '//*[@text="САМОВЫВОЗ"]'
    DELIVERY_PRICE_1 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]'
    DELIVERY_PRICE_2 = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_selector_view"]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.TextView[2]'
    ADDRESS = '//*[@resource-id="ru.limeshop.android.dev:id/delivery_info_title_text"]'
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
    ORDER_LIST_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/order_list_title_text"]'
    ORDER_LIST_SHEVRON = '//*[@resource-id="ru.limeshop.android.dev:id/order_list_chevron_image"]'
    SUMMARY_QUANTITY_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_quantity_title_text"]'
    SUMMARY_QUANTITY = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_quantity_text"]'
    SUMMARY_COAST_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_cost_title_text"]'
    SUMMARY_COAST = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_cost_text"]'
    SUMMARY_TOTAL_TITLE = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_total_title_text"]'
    SUMMARY_TOTAL = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_summary_total_text"]'
    ORDER_PAY = '//*[@resource-id="ru.limeshop.android.dev:id/order_pay_button"]'
    TERMS_TEXT = '//*[@resource-id="ru.limeshop.android.dev:id/checkout_terms_text"]'






