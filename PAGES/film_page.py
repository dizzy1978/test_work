from .base_page import BasePage
from .locators import MainPageLocators
from .locators import SearchResultsPageLocators
from .locators import FilmPageLocators


class FilmPage(BasePage):

    def should_be_film_page(self):  # Проверка что это страница фильма
        gotlink = self.browser.current_url
        assert gotlink == FilmPageLocators.FILM_URL, "Wrong film URL!"
        print("---Страница фильма идентифицирована")

    def check_film_title(self):  # Проверка названия фильма в карточке
        assert MainPageLocators.FILM_TITLE in SearchResultsPageLocators.SEARCH_TITLE, "Название фильма не совпадает с поиском!"
        print("---Название фильма проверено")

    def check_film_rating(self):  # Проверка рейтинга фильма в карточке
       assert SearchResultsPageLocators.SEARCH_RATING == FilmPageLocators.FILM_RATING, "Рейтинг фильма не совпадает с поиском!"
       print("---Рейтинг фильма проверен")
