from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json

browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/film/77331/"
browser.get(main_url)
time.sleep(10)
print (browser.current_url)
time.sleep(5)

SEARCH_AREA = browser.find_elements(By.XPATH, '//div[@class="styles_rowLight__P8Y_1 styles_row__da_RK"]')

j = {}
for e in SEARCH_AREA:
  list = e.text.split("\n")
















