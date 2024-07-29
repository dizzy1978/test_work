# Сохраняем все изображения
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/film/77331/stills/"
browser.get(main_url)
time.sleep(20)
n = 0
for i in browser.find_elements(By.TAG_NAME, "a"):
    n += 1
    if "/orig" in i.get_attribute('href'):
        img_src = i.get_attribute('href')
        img = requests.get(img_src)
        with open(rf"film_data\other_images\image_{n}.jpg", "wb") as file:
            file.write(img.content)

print("Film Images successfully saved")