# src/scraper.py
import time
import random
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from utils import get_data_file_writer, download_image

BASE_URL = "http://public.svstiming.cn/results.html?gameid=185&bib="
NUMBER_RANGES = {
    'A': [(1001, 1350), (2001, 2060)],
    'B': [(10001, 11050), (20001, 20450)]
}

def run_scraper(driver):
    '''Run the scraper for marathon data.'''
    with get_data_file_writer() as writer:
        for prefix in NUMBER_RANGES:
            for start, end in NUMBER_RANGES[prefix]:
                for i in range(start, end + 1):
                    bib_number = f"{prefix}{i}"
                    scrape_bib_number(driver, writer, bib_number)

def scrape_bib_number(driver, writer, bib_number):
    '''Scrape data for a specific bib number.'''
    url = f"{BASE_URL}{bib_number}"
    try:
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'eventtd')))
        time.sleep(random.randint(1, 2))
        
        event = driver.find_element(By.ID, 'eventtd').text or 'N/A'
        sex = driver.find_element(By.ID, 'grouptd').text or 'N/A'
        name = driver.find_element(By.ID, 'name').text or 'N/A'
        bib = driver.find_element(By.ID, 'bib').text or 'N/A'
        gun_time = driver.find_element(By.ID, 'result').text or 'N/A'
        net_time = driver.find_element(By.ID, 'netresult').text or 'N/A'

        writer.writerow([bib_number, event, sex, name, bib, gun_time, net_time])

        download_image(driver, bib_number)

    except (WebDriverException, NoSuchElementException) as e:
        log_file_path = Path(__file__).parent.parent / 'logs' / 'data_error.log'
        log_file_path.parent.mkdir(exist_ok=True)
        with open(log_file_path, 'a') as error_log:
            error_log.write(f'{bib_number}\n')

def retry_failed_bibs(driver):
    '''Retry scraping bibs that failed to scrape the first time.'''
    error_log_path = Path('logs/data_error.log')
    if not error_log_path.exists():
        print("No error log file found. Skipping retry.")
        return

    with error_log_path.open('r') as file:
        error_bibs = file.readlines()

    successful_retries = []
    with get_data_file_writer(file_name='data_error.csv') as writer:
        for bib in error_bibs:
            bib = bib.strip()
            try:
                scrape_bib_number(driver, writer, bib)
                successful_retries.append(bib)
            except Exception as e:
                log_error(bib, 'logs/data_error_2.log')

    with error_log_path.open('w') as file:
        for bib in error_bibs:
            if bib.strip() not in successful_retries:
                file.write(bib)

def log_error(bib_number, file_path):
    '''Log a bib number to a file.'''
    with open(file_path, 'a') as file:
        file.write(f'{bib_number}\n')