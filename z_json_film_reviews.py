# Парсим "О фильме", формируем словарь из него - JSON

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/film/77331/reviews/"
browser.get(main_url)
time.sleep(15)
print (browser.current_url, '\n')
time.sleep(5)




REVIEWS_BLOCK = browser.find_element(By.XPATH, "//ul[@class='resp_type']") # Весь div сводки по рецензиям
json_reviews = {}
for e in REVIEWS_BLOCK.find_elements(By.XPATH, "./li"):
    property = e.find_elements(By.XPATH, "./*")
    try:
        key = property[0].text
        value = property[1].text
        json_reviews[key] = value
    except:
        pass
with open(r'film_data\info\film_reviews_summary.json', 'w') as f:
    json.dump(json_reviews, f, ensure_ascii=False)
print("---Film_reviews_summary JSON file successfully saved")








