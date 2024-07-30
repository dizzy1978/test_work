# pytest -v --tb=line test_all_suite.py # Выводим только одну строку из лога каждого упавшего теста.
import pytest
import time
from .PAGES.main_page import MainPage
from PAGES.search_results_page import SearchResultsPage
from PAGES.film_page import FilmPage

base_link = "https://www.kinopoisk.ru"


def test_search_area_shuold_be_present_in_base_page(browser):
    page = MainPage(browser, base_link)
    page.open()
    page.should_be_search_area()

def test_searching_film(browser):
    page = MainPage(browser, base_link)
    page.open()
    page.do_film_search()

