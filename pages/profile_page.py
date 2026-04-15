from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):
    PROFILE_IMAGE = (By.CLASS_NAME, "profile__image")
    AVATAR_INPUT = (By.ID, "owner-avatar")
    SAVE_BUTTON = (By.XPATH, ".//form[@name='edit-avatar']/button[text()='Сохранить']")

    def click_profile_image(self):
        self.find(self.PROFILE_IMAGE).click()
        return self

    def update_avatar(self, avatar_url):
        avatar_input = self.wait_for_element(self.AVATAR_INPUT)
        avatar_input.clear()
        avatar_input.send_keys(avatar_url)
        self.find(self.SAVE_BUTTON).click()
        return self

    def get_avatar_style(self):
        return self.find(self.PROFILE_IMAGE).get_attribute('style')