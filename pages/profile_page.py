from pages.base_page import BasePage
from locators.locators import *


class ProfilePage(BasePage):

    url = 'https://qa-desk.stand.praktikum-services.ru/profile'

    def is_posted(self, name: str, city: str, price: int):
        self.is_visible(AD_CARD)
        assert name in (actual_name := self.find_element(AD_CARD_NAME).text), (
            f'Название не соответствует ожидаемому expected: {name}, actual: {actual_name}'
        )
        assert city in (actual_city := self.find_element(AD_CARD_CITY).text), (
            f'Город не соответствует ожидаемому expected: {city}, actual: {actual_city}'
        )
        assert str(price) in (actual_price := self.find_element(AD_CARD_PRICE).text), (
            f'Цена не соответствует ожидаемой expected: {price}, actual: {actual_price}'
        )
