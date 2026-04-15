import random
import pytest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.card_page import CardPage


class TestMesto:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver, "https://qa-mesto.praktikum-services.ru/")
        self.profile_page = ProfilePage(self.driver)
        self.card_page = CardPage(self.driver)

        # Авторизация перед каждым тестом
        self.login_page.open()
        self.login_page.login("email", "password")

    # проверка смены аватара
    def test_update_avatar(self):
        avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"

        self.profile_page.click_profile_image()
        self.profile_page.update_avatar(avatar_url)

        style = self.profile_page.get_avatar_style()
        assert avatar_url in style  # проверка обновления через атрибут style

    # создание и удаление карточки
    def test_create_and_delete_card(self):
        new_title = f"Москва{random.randint(100, 999)}"
        image_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenium.jpeg"

        # Запоминаем title последней карточки для проверки после удаления
        title_before = self.card_page.get_last_card_title()

        # Создаем новую карточку
        self.card_page.click_add_button()
        self.card_page.create_card(new_title, image_url)

        # Проверяем, что карточка создалась
        self.card_page.wait_for_card_title(new_title)
        title_after = self.card_page.get_first_card_title()
        assert title_after == new_title

        # Запоминаем количество карточек до удаления
        cards_before = self.card_page.get_cards_count()

        # Удаляем карточку
        self.card_page.delete_first_card()

        # Проверяем, что карточек стало на одну меньше
        self.card_page.wait_for_card_title(title_before)
        cards_after = self.card_page.get_cards_count()
        assert cards_before - cards_after == 1