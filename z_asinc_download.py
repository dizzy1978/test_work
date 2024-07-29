# Сохраняем все изображения асинхронно
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import uuid


browser = webdriver.Chrome()

main_url = "https://www.kinopoisk.ru/film/77331/stills/"
browser.get(main_url)
time.sleep(20)

# Формируем список урлов картинок
img_urls = []
n = 0
for i in browser.find_elements(By.TAG_NAME, "a"):
    n += 1
    if "/orig" in i.get_attribute('href'):
        img_src = i.get_attribute('href')
        img_urls.append(img_src)

# Функция скачивания и записи файла с уникальным именем
def download(url):
    img = requests.get(url)
    file_name = f'{uuid.uuid1()}.jpg'
    with open(rf"film_data\other_images\{file_name}.jpg", "wb") as file:
        file.write(img.content)
    print(f"Image {file_name}.jpg successfully saved")

# Асинхронный запуск максимум 16 потоков
with ThreadPoolExecutor(max_workers=16) as executor:
    executor.map(download, img_urls)




