from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')


class MainPageLocators:
    BASE_LINK = "https://www.kinopoisk.ru"
    SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')
    FILM_TITLE = "Ирония судьбы, или С легким паром"


class SearchResultsPageLocators:
    SEARCH_RESULT_PAGE_MARK = (By.XPATH, "//div[@class='search_results']")  # Должен содержать "Скорее всего, вы ищете"
    CORRECT_MARK = "Скорее всего, вы ищете"
    SEARCH_TITLE = (
    By.XPATH, "//a[contains(text(),'Ирония судьбы') and contains(text(),'С легким паром')]")  # link for click
    SEARCH_RATING = (By.XPATH,
                     "//div[@class='element most_wanted']/div[@class='right']/div[@class='rating  ratingGreenBG']")  # bad bad bad
    SEARCH_RELEASE = (By.XPATH, "//div[@class='element most_wanted']//span[@class='year']")  # so-so
    FILM_URL = "https://www.kinopoisk.ru/film/77331/"


class FilmPageLocators:
    FILM_URL = "https://www.kinopoisk.ru/film/77331/"
    FILM_TITLE = (By.XPATH, "//h1/span")  # Должен содержать название фильма из поиска/исходное
    FILM_RATING = (By.XPATH, "//span[contains(@class, 'film-rating-value')]/span[contains(@class, 'styles_rating')]")  # текст должен быть равен рейтингу из поиска
    FILM_RELEASE = (By.XPATH, "//a[contains(@href, 'lists/movies/year')]")
    POSTER_SRC = (By.XPATH, "//a[@class='styles_posterLink__C1HRc']/img")
    ABOUT_FILM_BLOCK = (By.XPATH, "//div[@{'data-test-id'}='encyclopedic-table']']")
    ALL_CHILD = (By.XPATH, "./*")
    IMAGES_LINK = (By.XPATH, "//a[@href='/film/77331/stills/' and text()[. ='Изображения']]")
    ALL_IMAGES_URL = "https://www.kinopoisk.ru/film/77331/stills/"
    REVIEWS_LINK = (By.XPATH, "_")
    REVIEWS_URL = "https://www.kinopoisk.ru/film/77331/reviews/"






