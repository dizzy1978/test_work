from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')


class MainPageLocators:
    SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')


class SearchResultsPageLocators:
    SEARCH_RESULT_PAGE_MARK = (By.XPATH, "//div[@class='search_results']")  # Должен содержать "Скорее всего, вы ищете"
    SEARCH_TITLE = (
    By.XPATH, "//a[contains(text(),'Ирония судьбы') and contains(text(),'С легким паром')]")  # for click
    SEARCH_RATING = (By.XPATH,
                     "//div[@class='element most_wanted']/div[@class='right']/div[@class='rating  ratingGreenBG']")  # bad bad bad
    SEARCH_RELEASE = (By.XPATH, "//div[@class='element most_wanted']//span[@class='year']")  # so-so


class FilmPageLocators:
    FILM_TITLE = (By.XPATH, "//h1/span")  # Должен содержать название фильма из поиска/исходное
    FILM_RATING = (By.XPATH, "//span[contains(@class, 'film-rating-value')]/span[contains(@class, 'styles_rating')]")  # текст должен быть равен рейтингу из поиска
    FILM_RELEASE = (By.XPATH, "//a[contains(@href, 'lists/movies/year')]")



