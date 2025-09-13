import pytest
from faker import Faker


class TestLoginAndRegister:

    @pytest.mark.xfail(reason='Баг - в адресе остается regiatration после регистрации')
    def test_register_user(self, main_page):
        fake = Faker()
        email = str(fake.email())
        password = str(fake.password())
        main_page.open_page(main_page.url)
        main_page.go_to_login()
        main_page.register_user(email, password)
        main_page.is_login()

    def test_register_user_invalid_email(self, main_page):
        fake = Faker()
        email = 'atyrlovamail.ru'
        password = str(fake.password())
        main_page.open_page(main_page.url)
        main_page.go_to_login()
        main_page.register_user(email, password)
        main_page.is_error('Ошибка')

    def test_register_user_already_exists(self, main_page, create_user):
        email, password = create_user
        main_page.logout()
        main_page.go_to_login()
        main_page.register_user(email, password)
        main_page.is_error('Ошибка')

    @pytest.mark.xfail(reason='Баг - в дефолтном имени пользователя лишняя точка в конце')
    def test_login(self, main_page, create_user):
        email, password = create_user
        main_page.open_page(main_page.url)
        main_page.go_to_login()
        main_page.login_user(email, password)
        main_page.is_login()

    def test_logout(self, main_page, create_user):
        main_page.logout()
        main_page.is_logout()
