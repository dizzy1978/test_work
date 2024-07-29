from .base_page import BasePage
from .locators import SearchResultsPageLocators

class SearchResultsPage(BasePage):

    def should_be_search_results_page(self):  # Проверка что это страница результатов поиска
        search_result_page_mark = (SearchResultsPageLocators.SEARCH_RESULT_PAGE_MARK)
        assert "Скорее всего, вы ищете" in search_result_page_mark, "Its not search results page"

    def do_click_on_founded_film(self): # Находим ссылку на искомый фильм и кликаем по ней, проверяем, что попали туда
        search_title_link = (SearchResultsPageLocators.SEARCH_TITLE)
        search_title_link.click()
        gotlink = self.browser.current_url
        assert gotlink == SearchResultsPageLocators.FILM_URL, "Wrong film URL!"



