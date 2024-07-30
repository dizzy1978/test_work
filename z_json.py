# Парсим "О фильме", формируем словарь из него - JSON

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/film/77331/"
browser.get(main_url)
time.sleep(15)
print (browser.current_url, '\n')
time.sleep(5)

ABOUT_FILM_BLOCK = browser.find_element(By.XPATH, "//div[@data-test-id='encyclopedic-table']") # Весь div карточки
print(ABOUT_FILM_BLOCK)
json_data = {}
for e in ABOUT_FILM_BLOCK.find_elements(By.XPATH, "./*"):
    print(e)
    property = e.find_elements(By.XPATH, "./*")
    key = property[0].text
    vals = property[1].find_elements(By.XPATH, "./*")
    valslist = [v.text for v in vals]
    json_data[key] = valslist
with open(r'film_data\info\film_data.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False)
print("Film_data JSON file successfully saved")








