from pages.film_page import FilmPage
from pages.main_page import MainPage


base_link = "https://www.kinopoisk.ru/"
film_link = "https://www.kinopoisk.ru/film/77331/"


# def test_do_search_film(browser):  # Working
#     page = MainPage(browser, base_link)
#     page.open()  # Working
#     page.do_film_search()  # Working
#     page.do_save_film_data_from_search_results_page()
#     page.do_click_on_founded_film()


# def test_check_film_page(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     time.sleep(15)
#     page.should_be_film_page()


# def test_check_film_title(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     time.sleep(15)
#     page.check_film_title()


# def test_check_saved_film_title(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.check_saved_film_title()
#
#
# def test_check_saved_film_rating(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.check_saved_film_rating()
#
#
# def test_check_saved_film_release_year(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.check_saved_film_release_year()


# def test_do_save_film_poster(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.do_save_film_poster()


# def test_do_save_film_info_to_JSON(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.do_save_film_info_to_json()


# def test_do_save_fullscreen_cs(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.do_save_fullscreen_cs_film_card()


# def test_do_save_images_async(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.do_async_save_film_images()


# def test_do_save_reviews_to_JSON(browser):  # Working
#     page = FilmPage(browser, film_link)
#     page.open()
#     page.do_save_reviews_summary()


