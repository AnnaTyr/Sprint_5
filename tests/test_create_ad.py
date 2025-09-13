
class TestCreateAd:

    def test_create_ad_unauthorised_user(self, main_page):
        main_page.open_page(main_page.url)
        main_page.go_to_create_ad()
        main_page.is_popup_to_authorise()

    def test_create_ad_authorised_user(self, main_page, create_user, create_ad_page, profile_page):
        name = 'Тестовое название'
        desc = 'Тестовое описание'
        price = 15
        category = 'Книги'
        city = 'Москва'
        main_page.go_to_create_ad()
        create_ad_page.create_new_ad(name, desc, price, category, city)
        main_page.go_to_profile()
        profile_page.wait_for_load_state()
        profile_page.is_posted(name, city, price)
