from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru"
browser.get(main_url)
time.sleep(15)




film_title = "Ирония судьбы, или С легким паром"

# Main_Page
browser.get(main_url)
time.sleep(15)
print (browser.current_url, '\n\n')
time.sleep(5)

SEARCH_AREA = browser.find_element(By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')
time.sleep(5)
SEARCH_AREA.send_keys(film_title)
time.sleep(5)

SUBMIT_BUTTON = browser.find_element(By.XPATH, '//button[@type="submit"]')
time.sleep(5)
SUBMIT_BUTTON.click()
time.sleep(15)


# Search_Results_Page
print(browser.current_url)

SEARCH_RESULT_PAGE_MARK = browser.find_element(By.XPATH, "//div[@class='search_results']")
print(SEARCH_RESULT_PAGE_MARK.text)

SEARCH_RATING = browser.find_element(By.XPATH,
                     "//div[@class='element most_wanted']/div[@class='right']/div[@class='rating  ratingGreenBG']")
print(SEARCH_RATING.text)

SEARCH_RELEASE = browser.find_element(By.XPATH, "//div[@class='element most_wanted']//span[@class='year']")
print(SEARCH_RELEASE.text, '\n\n')

SEARCH_TITLE = browser.find_element(By.XPATH, "//a[contains(text(),'Ирония судьбы') and contains(text(),'С легким паром')]")
time.sleep(5)
print(SEARCH_TITLE.text)
SEARCH_TITLE.click()
time.sleep(5)



# Film_Page
print(browser.current_url)
FILM_TITLE = browser.find_element(By.XPATH, "//h1/span")
title = FILM_TITLE.text
print(title)
time.sleep(5)

FILM_RATING = browser.find_element(By.XPATH, "//span[contains(@class, 'film-rating-value')]/span[contains(@class, 'styles_rating')]")
rat = FILM_RATING.text
print(rat)
time.sleep(5)

FILM_RELEASE = browser.find_element(By.XPATH, "//a[contains(@href, 'lists/movies/year')]")
rel = FILM_RELEASE.text
print(rel, '\n\n')
time.sleep(15)

IMAGES_LINK = browser.find_element(By.XPATH, "//a[@href='/film/77331/stills/' and text()[. ='Изображения']]")
time.sleep(5)
IMAGES_LINK.click()
time.sleep(5)
print(browser.current_url, '\n\n')








