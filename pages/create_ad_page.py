import time

from pages.base_page import BasePage
from locators.locators import *


class CreateAdPage(BasePage):

    url = 'https://qa-desk.stand.praktikum-services.ru/create-lisiting'

    def create_new_ad(self, name: str, desc: str, price: int, category: str, city: str):
        self.is_visible(INPUT_ITEM_NAME)
        self.find_element(INPUT_ITEM_NAME).send_keys(name)
        self.find_element(INPUT_ITEM_DESC).send_keys(desc)
        self.find_element(INPUT_ITEM_PRICE).send_keys(str(price))
        self.click(RADIO_CONDITION_BU)
        self.select_option_in_dropdown(DROPDOWN_CATEGORY, category)
        self.select_option_in_dropdown(DROPDOWN_CITY, city)
        self.click(BUTTON_POST_AD)
        time.sleep(1)

    def select_option_in_dropdown(self, dropdown: dict, option_text: str):
        self.click(dropdown)
        self.is_visible(DROPDOWN_MENU_OPTIONS)
        options = self.find_elements(OPTION_IN_DROPDOWN_MENU)
        for option in options:
            if option.text == option_text:
                option.click()
                return
        raise InterruptedError(f'{option_text} нет в выпадающем списке')
