# file: test_main.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Основной экран")
class TestMain:
    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Экран "Основной экран" / Скролл баннеров')
    @allure.testcase("C1861")
    def test_swipe_banner(self):
        page = BasePage()
        time.sleep(5)
        page.swipe_page_up()
        page.swipe_page_up()
        page.swipe_page_up()
        page.swipe_page_up()
        page.swipe_page_up()
        page.swipe_page_up()
        page.get_screen()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Экран "Авторизация" / Авторизация пользователя')
    @allure.testcase("C1016")
    def test_login(self):
        page = MainPage()
        page.login(valid_email, valid_password)

    @pytest.mark.main
    @pytest.mark.smoke
    @pytest.mark.demo
    @allure.title('Экран "Регистрация" / Заполнение полей "Имя/Фамилия" кириллицей')
    @allure.testcase("C1030")
    def test_reg(self):
        page = MainPage()
        page.user_registration()

    # @pytest.mark.main
    # @pytest.mark.smoke
    # @allure.title('Экран "Авторизация" / Авторизация пользователя по номеру телефона')
    # @allure.testcase("")
    # def test_login(self):
    #     page = MainPage()
    #     page.login_with_phone()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('TabBar / Цвет неактивных и активных иконок')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/197")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/194")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/3392")
    def test_reg(self):
        page = MainPage()
        page.icon_color_check(MainLocators.SEARCH_NAV)
        page.icon_color_check(MainLocators.FAVORITES_NAV)
        page.icon_color_catalog_check()
        page.icon_color_check(MainLocators.FAV_ICON)
        page.catalog.open_random_card()
        page.icon_color_check(ProductCardLocators.FAVORITE)
