# src/utils.py
import time
import random
import csv
import requests
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def choose_browser():
    '''Prompt user to choose a browser and return the corresponding WebDriver.'''
    browser_choice = input("Please enter the browser you want to use (Chrome, Edge, Firefox): ").lower()
    if browser_choice == 'chrome':
        return webdriver.Chrome()
    elif browser_choice == 'edge':
        return webdriver.Edge()
    elif browser_choice == 'firefox':
        return webdriver.Firefox()
    else:
        print("Invalid input, please enter Chrome, Edge, or Firefox.")
        return None

class DataFileWriter:
    '''Class to manage data file writing operations.'''
    def __init__(self, path):
        self.file = open(path, mode="a", newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        if self.file.tell() == 0:
            self.writer.writerow(["Bib Number(system)", "Event", "Sex", "Name", "Bib", "Gun Time", "Net Time"])

    def __enter__(self):
        return self.writer

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

def get_data_file_writer():
    '''Return a DataFileWriter instance for writing data to a CSV file.'''
    base_path = Path(__file__).parent.parent
    data_path = base_path / 'data'
    data_path.mkdir(exist_ok=True)
    data_file_path = data_path / 'data.csv'
    return DataFileWriter(data_file_path)

def download_image(driver, bib_number):
    '''Download and save the image for a given bib number.'''
    base_path = Path(__file__).parent.parent
    images_folder = base_path / 'images'
    images_folder.mkdir(exist_ok=True)

    try:
        download_button = driver.find_element(By.ID, 'downloadBtn')
        download_button.click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'img')))
        time.sleep(random.randint(2, 3))

        image = driver.find_element(By.TAG_NAME, 'img')
        image_url = image.get_attribute('src')

        response = requests.get(image_url)

        image_path = images_folder / f'{bib_number}.jpg'
        with open(image_path, 'wb') as picture_file:
            picture_file.write(response.content)

    except Exception:
        log_file_path = Path(__file__).parent.parent / 'logs' / 'picture_error.log'
        log_file_path.parent.mkdir(exist_ok=True)
        with open(log_file_path, 'a') as error_log:
            error_log.write(f'{bib_number}\n')

def get_data_file_writer(file_name='data.csv'):
    '''Return a DataFileWriter instance for writing data to a CSV file.'''
    base_path = Path(__file__).parent.parent
    data_path = base_path / 'data'
    data_path.mkdir(exist_ok=True)
    data_file_path = data_path / file_name
    return DataFileWriter(data_file_path)

def log_error(bib_number, file_path):
    '''Log a bib number to a file.'''
    with open(file_path, 'a') as file:
        file.write(f'{bib_number}\n')