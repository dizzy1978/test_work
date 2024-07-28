from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')


class MainPageLocators:
    SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')

class SearchResultsPageLocators:
    ITS_SEARCH_RESULT_PAGE = (By.XPATH, "//p[contains(text(),'Скорее всего, вы ищете')]")
    SEARCH_TITLE = (By.XPATH, "//a[contains(text(),'Ирония судьбы') and contains(text(),'С легким паром')]")
    # SEARH_RELEASE


#
# class FilmPageLocators:






# Локатор для всех 26 картинок: [class="styles_link__HN8dS"]