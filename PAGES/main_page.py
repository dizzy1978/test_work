import time

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import SearchResultsPageLocators


class MainPage(BasePage):

    def do_film_search(self):  # Передаем название фильма в поле поиска и ждем "Найти"
        search_area = self.browser.find_element(*MainPageLocators.SEARCH_AREA)
        search_area.send_keys(MainPageLocators.FILM_TITLE)
        submit_button = self.browser.find_element(*MainPageLocators.SUBMIT_BUTTON)
        submit_button.click()
        print("---Go to search results page")

    def should_be_search_results_page(self):  # Проверка что это страница результатов поиска
        search_result_page_mark = self.browser.find_element(SearchResultsPageLocators.SEARCH_RESULT_PAGE_MARK)
        assert (SearchResultsPageLocators.CORRECT_MARK) in search_result_page_mark, "Its not search results page!"
        print("---This is search results page")

    def do_save_film_data_from_search_results_page(self):
        film_data = []
        search_title = self.browser.find_element(*SearchResultsPageLocators.SEARCH_TITLE)
        film_data.append(search_title.text)
        film_data.append(';')
        search_rating = self.browser.find_element(*SearchResultsPageLocators.SEARCH_RATING)
        film_data.append(search_rating.text)
        film_data.append(';')
        search_release = self.browser.find_element(*SearchResultsPageLocators.SEARCH_RELEASE)
        film_data.append(search_release.text)
        film_data.append(';')
        with open(r"film_data\temp\film_data_temp.txt", "w") as file:
            print(*film_data, file=file)
        print("---Film data from search results Page saved to temp")

    def do_click_on_founded_film(self): # Находим ссылку на искомый фильм и кликаем по ней, проверяем, что попали туда
        search_title_link = self.browser.find_element(*SearchResultsPageLocators.SEARCH_TITLE)
        search_title_link.click()
        gotlink = self.browser.current_url
        assert SearchResultsPageLocators.FILM_URL in gotlink, "Wrong film URL!"
        print("---Film Page url correct")






