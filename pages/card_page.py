from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CardPage(BasePage):
    PLACES_LIST = (By.CLASS_NAME, "places__list")
    ADD_BUTTON = (By.CLASS_NAME, "profile__add-button")
    CARD_TITLE = (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']")
    FIRST_CARD_TITLE = (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']")
    NAME_INPUT = (By.NAME, "name")
    LINK_INPUT = (By.NAME, "link")
    SAVE_CARD_BUTTON = (By.XPATH, ".//form[@name='new-card']/button[text()='Сохранить']")
    DELETE_BUTTON = (By.XPATH,
                     "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']")
    ALL_CARDS = (By.XPATH, "//li[@class='places__item card']")

    def wait_for_places_list(self):
        self.wait_for_element(self.PLACES_LIST)
        return self

    def click_add_button(self):
        self.find(self.ADD_BUTTON).click()
        return self

    def get_last_card_title(self):
        cards = self.find_all(self.ALL_CARDS)
        last_card = cards[-1]
        return last_card.find_element(By.CLASS_NAME, "card__title").text

    def create_card(self, title, image_url):
        self.find(self.NAME_INPUT).send_keys(title)
        self.find(self.LINK_INPUT).send_keys(image_url)
        self.find(self.SAVE_CARD_BUTTON).click()
        return self

    def get_first_card_title(self):
        return self.find(self.FIRST_CARD_TITLE).text

    def get_cards_count(self):
        return len(self.find_all(self.ALL_CARDS))

    def delete_first_card(self):
        self.wait_for_clickable(self.DELETE_BUTTON).click()
        return self

    def wait_for_card_title(self, expected_title):
        self.wait_for_visible((By.XPATH, f"//h2[@class='card__title' and text()='{expected_title}']"))
        return self