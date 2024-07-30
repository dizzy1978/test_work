# Сохраняем постер
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

from pages.locators import FilmPageLocators

browser = webdriver.Chrome()

url = "https://www.kinopoisk.ru/film/77331/"
browser.get(url)
time.sleep(15)
poster_src = browser.find_element(*FilmPageLocators.POSTER_SRC)

img_src = poster_src.get_attribute("src")

img = requests.get(img_src)

with open(r"film_data\main_image\poster.jpg", "wb") as file:
    file.write(img.content)

print("Film Poster image successfully saved")