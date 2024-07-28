# Сохраняем постер
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/film/77331/"
browser.get(main_url)
time.sleep(15)
POSTER_SRC = browser.find_element(By.XPATH, "//a[@class='styles_posterLink__C1HRc']/img")
img_src = POSTER_SRC.get_attribute("src")

img = requests.get(img_src)

with open(r"film_data\main_image\poster.jpg", "wb") as file:
    file.write(img.content)
