from .base_page import BasePage
from .locators import MainPageLocators
from .locators import SearchResultsPageLocators
from .locators import FilmPageLocators
import requests


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

    def check_film_release_year(self):  # Проверка года выпуска фильма в карточке
       assert SearchResultsPageLocators.SEARCH_RELEASE == FilmPageLocators.FILM_RELEASE, "Год выпуска фильма не совпадает с поиском!"
       print("---Год выпуска фильма проверен")

    def do_save_film_poster(self):  # Сохраняем постер фильма (путь захардкожен, можно вынести в локаторы)
        poster_src = self.browser.find_element(FilmPageLocators.POSTER_SRC)
        img_src = poster_src.get_attribute("src")
        img = requests.get(img_src)
        with open(r"film_data\main_image\poster.jpg", "wb") as file:
            file.write(img.content)
        print("---Film Poster image successfully saved")

    def do_save_film_info_to_json(self):  # Сохраняем информацию из блока "О фильме" в JSON файл  (путь захардкожен, можно вынести в локаторы)




