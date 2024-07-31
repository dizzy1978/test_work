from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import FilmPageLocators
import requests
import json
import uuid
from concurrent.futures import ThreadPoolExecutor


class FilmPage(BasePage):

    def should_be_film_page(self):  # Проверка что это страница фильма
        gotlink = self.browser.current_url
        assert FilmPageLocators.FILM_URL in gotlink, "Wrong film Url!"
        print("---Film Url is OK")


    def check_film_title(self):  # Проверка названия фильма в карточке
        search_title = self.browser.find_element(*FilmPageLocators.FILM_TITLE)
        assert MainPageLocators.FILM_TITLE in search_title.text, "Wrong film Title!"
        print("---Film Title is OK")


    def check_saved_film_title(self):  # Сравнение названия фильма с поиском
        with open(r"film_data\temp\film_data_temp.txt", "r") as file:
            for string in file:
                data = string.split(';')
        saved_title = data[0].strip().strip(")")
        search_title = self.browser.find_element(*FilmPageLocators.FILM_TITLE)
        assert saved_title in search_title.text, "Film Title not same with searched!"
        print("---Film Title same with searched")


    def check_saved_film_rating(self):  # Сравнение рейтинга фильма с поиском
        with open(r"film_data\temp\film_data_temp.txt", "r") as file:
            for string in file:
                data = string.split(';')
        saved_rating = data[1].strip()
        search_rating = self.browser.find_element(*FilmPageLocators.FILM_RATING)
        assert saved_rating in search_rating.text, "Film Rating not same with searched!"
        print("---Film Rating same with searched")


    def check_saved_film_release_year(self):  # Сравнение года выпуска фильма с поиском
        with open(r"film_data\temp\film_data_temp.txt", "r") as file:
            for string in file:
                data = string.split(';')
        saved_year = data[2].strip()
        search_year = self.browser.find_element(*FilmPageLocators.FILM_RELEASE)
        assert saved_year in search_year.text, "Film release Year not same with searched!"
        print("---Film release Year same with searched")


    # Сохраняем постер фильма
    def do_save_film_poster(self):   # путь захардкожен, можно вынести в локаторы/генерить. Линукс. os.makedirs(dir).
        poster_src = self.browser.find_element(*FilmPageLocators.POSTER_SRC)
        img_src = poster_src.get_attribute("src")
        img = requests.get(img_src)
        with open(r"film_data\main_image\poster.jpg", "wb") as file:
            file.write(img.content)
        print("---Film Poster image successfully saved")


    # Сохраняем инфо из блока "О фильме" в JSON файл
    def do_save_film_info_to_json(self):    # путь захардкожен, лучше создавать. Слэши под Линукс
        about_film_block = self.browser.find_element(*FilmPageLocators.ABOUT_FILM_BLOCK)  # Общий div блока
        json_data = {}
        for e in about_film_block.find_elements(*FilmPageLocators.ALL_CHILD):
            property = e.find_elements(*FilmPageLocators.ALL_CHILD)
            key = property[0].text
            vals = property[1].find_elements(*FilmPageLocators.ALL_CHILD)
            valslist = [v.text for v in vals]
            json_data[key] = valslist
        with open(r'film_data\info\film_data.json', 'w') as f:
            json.dump(json_data, f, ensure_ascii=False)
        print("---Film data JSON-file successfully saved")


    # Сохраняем fullscreen браузера страницы фильма
    def do_save_fullscreen_cs_film_card(self):
        fs = self.browser.find_element(*FilmPageLocators.TAG_NAME_BODY)
        png = fs.screenshot_as_png
        with open(r"film_data\other_images\fullscreen.png", "wb") as file:   # путь захардкожен, лучше создавать
            file.write(png)
        print("---Fullscreen screenshot film Page successfully saved")


    # Асинхронно сохраняем картинки в файлы с уникальными именами
    def do_async_save_film_images(self):
        images_link = self.browser.find_element(*FilmPageLocators.IMAGES_LINK)
        images_link.click()
        # Формируем список урлов картинок
        img_urls = []
        for i in self.browser.find_elements(*FilmPageLocators.TAG_NAME_A):
            if "/orig" in i.get_attribute('href'):
                img_src = i.get_attribute('href')
                img_urls.append(img_src)
        # Функция скачивания и записи файла с уникальным именем
        def download(url):
            img = requests.get(url)
            file_name = f'{uuid.uuid1()}.jpg'
            with open(rf"film_data\other_images\{file_name}.jpg", "wb") as file:
                file.write(img.content)
            print(f"Image {file_name}.jpg successfully saved")
        # Запуск многопоточного скачивания, максимум 16 потоков
        with ThreadPoolExecutor(max_workers=16) as executor:
            executor.map(download, img_urls)


    # Сохраняем сводку по рецензиям в JSON файл
    def do_save_reviews_summary(self):
        reviews_link = self.browser.find_element(*FilmPageLocators.REVIEWS_LINK)
        reviews_link.click()
        reviews_block = self.browser.find_element(*FilmPageLocators.REVIEWS_BLOCK)
        json_reviews = {}
        for e in reviews_block.find_elements(*FilmPageLocators.ALL_CHILD_LI):
            property = e.find_elements(*FilmPageLocators.ALL_CHILD)
            try:
                key = property[0].text
                value = property[1].text
                json_reviews[key] = value
            except:
                pass
        with open(r'film_data\info\film_reviews_summary.json', 'w') as f:
            json.dump(json_reviews, f, ensure_ascii=False)
        print("---Film_reviews_summary JSON file successfully saved")


