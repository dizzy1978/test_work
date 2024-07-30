import pytest
import time
from pages.film_page import FilmPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage

base_link = "https://www.kinopoisk.ru/"
film_link = "https://www.kinopoisk.ru/film/77331/"

def test_do_search_film(browser):
    page = MainPage(browser, base_link)
    page.open()
    page.do_film_search()
    #page.should_be_search_results_page()
    #page.do_click_on_founded_film()


def test_founded_film(browser):
    page = FilmPage(browser, film_link)
    page.open()
    page.should_be_film_page()


# def test_check_film_title(browser):
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.check_film_title()


# def test_check_film_rating(browser):
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.check_film_rating()
#
#
# def test_check_film_release_year(browser):
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.check_film_release_year()

