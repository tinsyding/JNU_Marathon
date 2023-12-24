#单文件版本
import os
import time
import random
import csv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import requests

BASE_URL = "http://public.svstiming.cn/results.html?gameid=185&bib="

NUMBER_RANGES = {
    'A': [(1001, 1350), (2001, 2060)],
    'B': [(10001, 11050), (20001, 20450)]
}

driver = webdriver.Chrome()
# driver = webdriver.Edge()
# driver = webdriver.Firefox()

data_dir = Path(__file__).parent / 'data'
images_dir = Path(__file__).parent / 'images'
log_dir = Path(__file__).parent / 'logs'

# create directories if they do not exist
os.makedirs(data_dir, exist_ok=True)
os.makedirs(images_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

with open(data_dir / 'data.csv', mode="a", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["Bib Number(system)", "Event", "Sex", "Name", "Bib", "Gun Time", "Net Time"])

    for prefix in NUMBER_RANGES:
        for start, end in NUMBER_RANGES[prefix]:
            for i in range(start, end + 1):
                bib_number = f"{prefix}{i}"
                url = f"{BASE_URL}{bib_number}"
                try:
                    driver.get(url)
                    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'eventtd')))
                    time.sleep(random.randint(1, 2))

                    event = driver.find_element(By.ID, 'eventtd').text or 'N/A'
                    sex = driver.find_element(By.ID, 'grouptd').text or 'N/A'
                    name = driver.find_element(By.ID, 'name').text or 'N/A'
                    bib = driver.find_element(By.ID, 'bib').text or 'N/A'
                    gun_time = driver.find_element(By.ID, 'result').text or 'N/A'
                    net_time = driver.find_element(By.ID, 'netresult').text or 'N/A'

                    writer.writerow([bib_number, event, sex, name, bib, gun_time, net_time])
                    
                    download_button = driver.find_element(By.ID, 'downloadBtn')
                    download_button.click()
                    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'img')))
                    time.sleep(random.randint(2, 3))

                    image = driver.find_element(By.TAG_NAME, 'img')
                    image_url = image.get_attribute('src')

                    response = requests.get(image_url)

                    image_path = images_dir / f'{bib_number}.jpg'
                    with open(image_path, 'wb') as picture_file:
                        picture_file.write(response.content)

                except (WebDriverException, NoSuchElementException) as e:
                    with open(log_dir / 'data_error.log', 'a') as log_file:
                        log_file.write(f"{bib_number}\n")

driver.quit()