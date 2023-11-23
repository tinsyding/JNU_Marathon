# src/main.py
from scraper import run_scraper
from utils import choose_browser

def main():
    '''Main function to run the scraper'''
    driver = None
    driver = choose_browser()
    run_scraper(driver)
    if driver:
        driver.quit()
                
if __name__ == "__main__":
    main()