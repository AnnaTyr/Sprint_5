from pages.base_page import BasePage
from locators.locators import *


class MainPage(BasePage):

    url = 'https://qa-desk.stand.praktikum-services.ru'
    
    def go_to_login(self):
        self.wait_for_load_state()
        self.click(BUTTON_LOGIN_AND_REGISTER)
        self.url_contains('/login')
    
    def register_user(self, email: str, password: str):
        self.click(BUTTON_NO_ACCOUNT)
        self.url_contains('/regiatration')
        self.is_visible(BUTTON_CREATE_ACCOUNT)
        self.find_element(INPUT_EMAIL).send_keys(email)
        self.find_element(INPUT_PASSWORD).send_keys(password)
        self.find_element(INPUT_SUBMIT_PASSWORD).send_keys(password)
        self.click(BUTTON_CREATE_ACCOUNT)

    def login_user(self, email: str, password: str):
        self.is_visible(BUTTON_LOGIN)
        self.find_element(INPUT_EMAIL).send_keys(email)
        self.find_element(INPUT_PASSWORD).send_keys(password)
        self.click(BUTTON_LOGIN)

    def go_to_create_ad(self):
        self.wait_for_load_state()
        self.click(BUTTON_CREATE_AD)

    def go_to_profile(self):
        self.wait_for_load_state()
        self.click(BUTTON_AVATAR)
        self.wait_for_load_state()

    def is_login(self):
        assert 'regiatration' not in self.driver.current_url
        assert self.is_visible(BUTTON_CREATE_AD)
        assert self.is_visible(BUTTON_AVATAR)
        assert (actual := self.find_element(USER_NAME).text) == 'User', \
            f'Текст не соответствует ожидаемому - expected: User, actual: {actual}'

    def is_error(self, error_message):
        assert self.is_visible(ERROR_MESSAGE)
        assert self.find_element(ERROR_MESSAGE).text == error_message
        assert len(self.find_elements(INPUT_WITH_ERROR)) == 3

    def logout(self):
        self.wait_for_load_state()
        self.click(BUTTON_LOGOUT)

    def is_logout(self):
        assert self.is_visible(BUTTON_LOGIN_AND_REGISTER)

    def is_popup_to_authorise(self):
        assert self.is_visible(HEADER_POPUP)
        assert self.find_element(HEADER_POPUP).text == 'Чтобы разместить объявление, авторизуйтесь'
