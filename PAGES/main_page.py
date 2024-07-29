from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_search_area(self):  # Проверка наличия поля поиска
        assert self.is_element_present(MainPageLocators.SEARCH_AREA,
                                       MainPageLocators.BASE_LINK), "Search area is not presented!"
        print("---Поле поиска найдено")

    def do_film_search(self):  # Передаем название фильма в поиск и ждем "Найти"
        search_area = self.browser.find_element(MainPageLocators.SEARCH_AREA)
        search_area.send_keys(MainPageLocators.FILM_TITLE)
        submit_button = self.browser.find_element(MainPageLocators.SUBMIT_BUTTON)
        submit_button.click()
        print("---Переходим на страницу фильма")





