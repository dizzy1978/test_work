from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/"
film_title = "Ирония судьбы, или С легким паром"

browser.get(main_url)
time.sleep(15)
search_area = browser.find_element(By.XPATH, '//*[@placeholder="Фильмы, сериалы, персоны"]')
time.sleep(5)
search_area.send_keys(film_title)
time.sleep(5)
submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
time.sleep(5)
submit_button.click()
time.sleep(5)
ITS_SEARCH_RESULT_PAGE = browser.find_element(By.XPATH, "//p[contains(text(),'Скорее всего, вы ищете')]")







# SEARCH_TITLE = browser.find_element(By.XPATH, "//a[contains(text(),'Ирония судьбы') and contains(text(),'С легким паром')]")
# time.sleep(5)
# SEARCH_TITLE.click()
# time.sleep(15)











