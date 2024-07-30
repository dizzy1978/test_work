# pytest -v --tb=line test_product_page.py # Выводим только одну строку из лога каждого упавшего теста.
import pytest
import time
from .PAGES.main_page import MainPage
from .pages.search_results_page import SearchResultsPage
from .pages.login_page import LoginPage

def search_area_is_present(browser):
    page = MainPage(browser, link)

    pass

