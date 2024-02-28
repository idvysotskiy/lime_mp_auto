# file: test_main.py
import pytest
from pages.main_page import MainPage
from pages.base_page import *
import allure


@pytest.fixture(autouse=True)
def clear_app(device):
    yield
    device.app_clear(package)


class TestMobile:
    @pytest.mark.smoke
    @allure.title('Экран "Основной экран" / Скролл баннеров')
    @allure.testcase("C1861")
    def test_swipe_banner(self, device):
        page = BasePage(device)
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
    def test_login(self, device):
        page = MainPage(device)
        page.login(valid_email, valid_password)

    @pytest.mark.smoke
    @allure.title('Экран "Коллекции" / Добавление в избранное (добавление в список) с экрана "Коллекция"')
    @allure.testcase("C283")
    def test_add_to_fav_from_catalog(self, device):
        page = MainPage(device)
        page.click_to_nav_catalog()
        page.go_to_catalog_item(menu_l1)
        page.add_to_fav_from_catalog()

    @pytest.mark.smoke
    @allure.title('Экран "Регистрация" / Заполнение полей "Имя/Фамилия" кириллицей')
    @allure.testcase("C1030")
    def test_reg(self, device):
        page = MainPage(device)
        page.go_to_registration()
        page.enter_valid_registration_data(valid_name_kir, valid_surname_kir, valid_phone, valid_password)
        page.click_subscribe_boxes(subscribe)
        page.click_resume_btn_signup()
        page.cancel_notification()
        page.screen_title('ЛИЧНЫЙ КАБИНЕТ')


