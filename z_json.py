from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json

browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/film/77331/"
browser.get(main_url)
time.sleep(15)
print (browser.current_url)
time.sleep(5)

SEARCH_AREA = browser.find_element(By.XPATH, f"//div[@{'data-test-id'}='encyclopedic-table']") # Весь div карточки
json_data = {}
for e in SEARCH_AREA.find_elements(By.XPATH, "./*"):
    property = e.find_elements(By.XPATH, "./*")
    key = property[0].text
    vals = property[1].find_elements(By.XPATH, "./*")
    valslist = [v.text for v in vals]
    json_data[key] = valslist

with open(r'film_data\info\film_data.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False)


print("Film_data JSON file successfully saved")








