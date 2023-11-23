# src/main.py
from scraper import run_scraper
from utils import choose_browser

def main():
    '''
    Main function to initialize the WebDriver and run the scraper.
    - Chooses a browser based on user input.
    - Initializes the WebDriver for the selected browser.
    - Calls the run_scraper function to execute the scraping process.
    '''
    driver = None
    driver = choose_browser()
    run_scraper(driver)
    if driver:
        driver.quit()
                
if __name__ == "__main__":
    main()