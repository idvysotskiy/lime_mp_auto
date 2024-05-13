import pytest
from pages.main_page import MainPage
import allure


@pytest.mark.usefixtures("setup")
@allure.feature("Профиль")
class TestProfile:
    @allure.title('Экран "Личный кабинет" (Пользователь не авторизован)')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/16")
    @pytest.mark.profile
    def test_account_without_authorization(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.checking_account_elements()

    @allure.title('Экран "Личный кабинет" / Выход с экрана')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/317")
    @pytest.mark.profile
    def test_closing_account(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.close_account()
        page.wait_logo()

    @allure.title('Экран "Личный кабинет" / Кнопка "Руководство по покупке"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/318")
    @pytest.mark.profile
    def test_manual(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.open_manual()

    @allure.title('Экран "Личный кабинет" / Кнопка "Контакты"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/319")
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/1901")
    @pytest.mark.profile
    def test_contacts(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.open_contacts()
        page.profile.checking_contacts_phone_number()

    @allure.title('Экран "Личный кабинет" / Кнопка "Компания"')
    @allure.testcase("https://lmdev.testrail.io/index.php?/cases/view/320")
    @pytest.mark.profile
    def test_about_company(self, connect_to_device):
        page = MainPage(connect_to_device)
        page.open_profile()
        page.profile.open_company()



