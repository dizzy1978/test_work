# Сохраняем full-screen окно браузера

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()

url = "https://www.kinopoisk.ru/film/77331/"
path_to_save = r"film_data\other_images\fullscreen.png"

browser.get(url)
browser.maximize_window()
time.sleep(15)

fs = browser.find_element(By.TAG_NAME, "body")
png = fs.screenshot_as_png
with open(path_to_save, "wb") as file:
    file.write(png)

print("---Fullscreen screenshot film Page successfully saved")

