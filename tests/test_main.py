# file: test_main.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.fixture(autouse=True)
def clear_app(d):
    MainPage(d).set_nuxt_02()
    MainPage(d).login(valid_email, valid_password)
    MainPage(d).set_feature_toggles()
    time.sleep(2)
    yield
    d.app_clear(package)


class TestMobile:
    @pytest.mark.smoke
    @allure.title('Экран "Основной экран" / Скролл баннеров')
    @allure.testcase("C1861")
    def test_swipe_banner(self, d):
        page = BasePage(d)
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
    def test_login(self, d):
        page = MainPage(d)
        page.login(valid_email, valid_password)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Добавление в избранное (добавление в список) с экрана "Коллекция"')
    @allure.testcase("C283")
    def test_add_to_fav_from_catalog(self, d):
        page = MainPage(d)
        page.click_to_nav_catalog()
        page.go_to_catalog_item(menu_l1)
        page.add_to_fav_from_catalog()

    @pytest.mark.smoke
    @allure.title('Экран "Регистрация" / Заполнение полей "Имя/Фамилия" кириллицей')
    @allure.testcase("C1030")
    def test_reg(self, d):
        page = MainPage(d)
        page.go_to_registration()
        page.enter_valid_registration_data(valid_name_kir, valid_surname_kir, valid_phone, valid_password)
        page.click_subscribe_boxes(subscribe)
        page.click_resume_btn_signup()
        page.cancel_notification()
        page.screen_title('ЛИЧНЫЙ КАБИНЕТ')


