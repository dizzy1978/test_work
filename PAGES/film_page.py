from .base_page import BasePage
from .locators import MainPageLocators
from .locators import SearchResultsPageLocators
from .locators import FilmPageLocators
import requests
import json


class FilmPage(BasePage):

    def should_be_film_page(self):  # Проверка что это страница фильма
        gotlink = self.browser.current_url
        assert FilmPageLocators.FILM_URL in gotlink, "Wrong film Url!"
        print("---Film Url is OK")

    def check_film_title(self):  # Проверка названия фильма в карточке
        assert MainPageLocators.FILM_TITLE in SearchResultsPageLocators.SEARCH_TITLE, "Wrong film Title!"
        print("---Film Title is OK")

    def check_film_rating(self):  # Проверка рейтинга фильма в карточке
        assert SearchResultsPageLocators.SEARCH_RATING == FilmPageLocators.FILM_RATING, "Wrong film Rating!"
        print("---Film Rating is OK")

    def check_film_release_year(self):  # Проверка года выпуска фильма в карточке
        assert SearchResultsPageLocators.SEARCH_RELEASE == FilmPageLocators.FILM_RELEASE, "Wrong film release Year!"
        print("---Film Release year is OK")

    def do_save_film_poster(self):  # Сохраняем постер фильма (путь захардкожен, можно вынести в локаторы/генерить. Линукс. os.makedirs(dir). )
        poster_src = self.browser.find_element(FilmPageLocators.POSTER_SRC)
        img_src = poster_src.get_attribute("src")
        img = requests.get(img_src)
        with open(r"film_data\main_image\poster.jpg", "wb") as file:
            file.write(img.content)
        print("---Film Poster image successfully saved")

    def do_save_film_info_to_json(self):  # Сохраняем инфо из блока "О фильме" в JSON файл  (путь захардкожен, лучше создавать. Слэши под Линукс)
        about_film_block = self.browser.find_element(FilmPageLocators.ABOUT_FILM_BLOCK)  # Общий div блока
        json_data = {}
        for e in about_film_block.find_elements(FilmPageLocators.ALL_CHILD):
            property = e.find_elements(FilmPageLocators.ALL_CHILD)
            key = property[0].text
            vals = property[1].find_elements(FilmPageLocators.ALL_CHILD)
            valslist = [v.text for v in vals]
            json_data[key] = valslist
        with open(r'film_data\info\film_data.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False)
        print("---Film data JSON-file successfully saved")

    def go_to_images_inset(self):  # Переходим на вкладку "Изображения"
        images_link = self.browser.find_element(FilmPageLocators.IMAGES_LINK)
        images_link.click()
        gotlink = self.browser.current_url
        assert FilmPageLocators.ALL_IMAGES_URL in gotlink, "Wrong film images URL!"
        print("---Images Inset successfully opened")
