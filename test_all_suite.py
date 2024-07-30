import pytest
import time
from pages.film_page import FilmPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage

base_link = "https://www.kinopoisk.ru/"
film_link = "https://www.kinopoisk.ru/film/77331/"

# def test_do_search_film(browser):
#     page = MainPage(browser, base_link)  # Working
#     page.open()  # Working
#     page.do_film_search()  # Working
#     #page.should_be_search_results_page()
#     #page.do_click_on_founded_film()


# def test_founded_film_page(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     time.sleep(15)
#     page.should_be_film_page()


# def test_check_film_title(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     time.sleep(15)
#     page.check_film_title()


# def test_check_film_rating(browser):
#     pass

# def test_check_film_release_year(browser):
#     pass


# def test_do_save_film_poster(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.do_save_film_poster()

def test_do_save_film_info_to_JSON(browser):
    page = FilmPage(browser, film_link)
    page.open()
    page.do_save_film_info_to_json()
