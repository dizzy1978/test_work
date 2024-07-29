# Сохраняем все изображения
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/film/77331/stills/"
browser.get(main_url)
time.sleep(15)

ALL_IMAGES = browser.find_elements(By.XPATH, "//div[@class = 'styles_root__eTXf4 styles_gallery__LodYs styles_threeColumns__r1OOn']//descendant::img")

for img in ALL_IMAGES:
    img_sorce = img.get_attribute("src")
    print(img_sorce)
#
# img = requests.get(img_src)
#
#
# with open(r"film_data\main_image\poster.jpg", "wb") as file:
#     file.write(img.content)
