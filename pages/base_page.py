from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement

from locators.locators import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_state(self):
        self.is_visible(BOTTOM_LOCATOR)
        self.is_clickable(BOTTOM_LOCATOR)

    def open_page(self, url: str):
        self.driver.get(url)

    def find_element(self, locator: dict) -> WebElement:
        try:
            element = self.driver.find_element(by=locator['locator'][0], value=locator["locator"][1])
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент \"{locator['name']}\" не найден на странице")

    def find_elements(self, locator: dict):
        try:
            return self.driver.find_elements(by=locator['locator'][0], value=locator["locator"][1])
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент \"{locator['name']}\" не найден на странице")

    def is_visible(self, locator: dict, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator['locator']))

    def is_clickable(self, locator: dict, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator['locator']))

    def click(self, locator: dict):
        element = self.find_element(locator)
        if self.is_clickable(locator):
            element.click()
        else:
            raise NoSuchElementException('Элемент не кликабелен')

    def url_contains(self, url: str, timeout: int = 3):
        WebDriverWait(self.driver, timeout).until(ec.url_contains(url))

