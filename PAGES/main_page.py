from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_search_area(self): # Проверка наличия поля поиска
        assert self.is_element_present(*MainPageLocators.SEARCH_AREA), "Search area is not presented!"

    def do_film_search(self, film_title): # Передаем название фильма в поиск и ждем "Найти"
        search_area = self.browser.find_element(*MainPageLocators.SEARCH_AREA)
        search_area.send_keys(film_title)
        submit_button = self.browser.find_element(*MainPageLocators.SUBMIT_BUTTON)
        submit_button.click()

