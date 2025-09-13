from selenium.webdriver.common.by import By

BUTTON_LOGIN_AND_REGISTER = {
    'locator': (By.XPATH, '//button[text()="Вход и регистрация"]'),
    'name': 'Кнопка Вход и регистрация'
}
INPUT_EMAIL = {
    'locator': (By.XPATH, '//input[@name="email"]'),
    'name': 'Поле ввода email'
}
INPUT_PASSWORD = {
    'locator': (By.XPATH, '//input[@name="password"]'),
    'name': 'Поле ввода пароля'
}
INPUT_SUBMIT_PASSWORD = {
    'locator': (By.XPATH, '//input[@name="submitPassword"]'),
    'name': 'Поле ввода пароля повторно'
}
BUTTON_LOGIN = {
    'locator': (By.XPATH, '//button[text()="Войти"]'),
    'name': 'Кнопка Войти'
}
BUTTON_NO_ACCOUNT = {
    'locator': (By.XPATH, '//button[text()="Нет аккаунта"]'),
    'name': 'Кнопка Нет аккаунта'
}
BUTTON_CREATE_ACCOUNT = {
    'locator': (By.XPATH, '//button[text()="Создать аккаунт"]'),
    'name': 'Кнопка Создать аккаунт'
}
USER_NAME = {
    'locator': (By.XPATH, '//h3[@class="profileText name"]'),
    'name': 'Имя пользователя'
}
BUTTON_AVATAR = {
    'locator': (By.XPATH, '//button[@class="circleSmall"]'),
    'name': 'Аватар пользователя'
}
BUTTON_CREATE_AD = {
    'locator': (By.XPATH, '//button[text()="Разместить объявление"]'),
    'name': 'Кнопка Разместить объявление'
}
ERROR_MESSAGE = {
    'locator': (By.XPATH, '//span[contains(@class, "input_span")]'),
    'name': 'Ошибка'
}
INPUT_WITH_ERROR = {
    'locator': (By.XPATH, '//div[contains(@class, "inputError")]'),
    'name': 'Поле ввода подсвеченное красным'
}
BUTTON_LOGOUT = {
    'locator': (By.XPATH, '//button[text()="Выйти"]'),
    'name': 'Кнопка Выйти'
}
HEADER_POPUP = {
    'locator': (By.XPATH, '//div[contains(@class, "popUp_titleRow")]/h1'),
    'name': 'Заголовок попапа'
}
INPUT_ITEM_NAME = {
    'locator': (By.XPATH, '//input[@name="name"]'),
    'name': 'Поле ввода названия'
}
INPUT_ITEM_DESC = {
    'locator': (By.XPATH, '//textarea[@name="description"]'),
    'name': 'Поле ввода описания товара'
}
INPUT_ITEM_PRICE = {
    'locator': (By.XPATH, '//input[@name="price"]'),
    'name': 'Поле ввода цены'
}
DROPDOWN_CATEGORY = {
    'locator': (By.XPATH, '//input[@name="category"]/../button'),
    'name': 'Выпадающий список Категория'
}
DROPDOWN_CITY = {
    'locator': (By.XPATH, '//input[@name="city"]/../button'),
    'name': 'Выпадающий список Город'
}
DROPDOWN_MENU_OPTIONS = {
    'locator': (By.XPATH, '//div[contains(@class, "dropDownMenu_options")]'),
    'name': 'Варианта в выпадающем списке'
}
OPTION_IN_DROPDOWN_MENU = {
    'locator': (By.XPATH, '//button[contains(@class, "dropDownMenu_btn")]'),
    'name': 'Вариант в выпадающем списке'
}
RADIO_CONDITION_BU = {
    'locator': (By.XPATH, '//input[@value="Б/У"]/../div'),
    'name': 'Радио-баттон Б/У'
}
BUTTON_POST_AD = {
    'locator': (By.XPATH, '//button[text()="Опубликовать"]'),
    'name': 'Кнопка Опубликовать'
}
AD_CARD = {
    'locator': (By.XPATH, '//div[@class="card"]'),
    'name': 'Объявление'
}
AD_CARD_NAME = {
    'locator': (By.XPATH, '//div[@class="about"]/h2'),
    'name': 'Название товара в объявлении'
}
AD_CARD_CITY = {
    'locator': (By.XPATH, '//div[@class="about"]/h3'),
    'name': 'Город в объявлении'
}
AD_CARD_PRICE = {
    'locator': (By.XPATH, '//div[@class="price"]/h2'),
    'name': 'Цена в объявлении'
}
HEADER_PROFILE = {
    'locator': (By.XPATH, '//h1[text()="Мой профиль"]'),
    'name': 'Цена в объявлении'
}
BOTTOM_LOCATOR = {
    'locator': (By.XPATH, '//a[text()="О нас"]'),
    'name': 'Локатор внизу страницы'
}
