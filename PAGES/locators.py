from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')


class MainPageLocators:
    SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@type="submit"]')

class SearchResultsPageLocators:
    SEARCH_TITLE = (By.XPATH, "//a[contains(text(),'Ирония судьбы') and contains(text(),'С легким паром')]")
    # SEARCH_RATING
    # SEARH_RELEASE


#
# class FilmPageLocators:
#     SEARCH_AREA = (By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')









#//a[contains(text(),'Ирония судьбы') and contains(text(),'С легким паром')]
# Локатор для всех 26 картинок: [class="styles_link__HN8dS"]