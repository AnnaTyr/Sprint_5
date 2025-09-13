import pytest
from faker import Faker
from selenium import webdriver
from pages.main_page import MainPage
from pages.create_ad_page import CreateAdPage
from pages.profile_page import ProfilePage
from locators.locators import BUTTON_LOGOUT


@pytest.fixture(scope='function')
def create_driver():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def main_page(create_driver):
    """
    Открывает страницу логина
    """
    page = MainPage(create_driver)
    return page


@pytest.fixture(scope='function')
def create_ad_page(create_driver):
    """
    Открывает страницу создания объявления
    """
    page = CreateAdPage(create_driver)
    return page


@pytest.fixture(scope='function')
def profile_page(create_driver):
    """
    Открывает страницу создания объявления
    """
    page = ProfilePage(create_driver)
    return page


@pytest.fixture(scope='function')
def create_user(main_page):
    """
    Создает нового пользователя
    """
    fake = Faker()
    email = str(fake.email())
    password = str(fake.password())

    main_page.open_page(main_page.url)
    main_page.go_to_login()
    main_page.register_user(email, password)
    main_page.is_visible(BUTTON_LOGOUT)
    return email, password
