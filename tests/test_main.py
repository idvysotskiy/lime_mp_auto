# file: test_main.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.mark.usefixtures("setup")
class TestMobile:
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

    @pytest.mark.smoke
    @allure.title('Экран "Авторизация" / Авторизация пользователя')
    @allure.testcase("C1016")
    def test_login(self):
        page = MainPage()
        page.login(valid_email, valid_password)

    @pytest.mark.smoke
    @allure.title('Экран "Регистрация" / Заполнение полей "Имя/Фамилия" кириллицей')
    @allure.testcase("C1030")
    def test_reg(self):
        page = MainPage()
        page.reg_kir()
        page.screen_title('ЛИЧНЫЙ КАБИНЕТ')
