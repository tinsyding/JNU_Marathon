# src/main.py
from selenium.common.exceptions import WebDriverException
from scraper import run_scraper
from utils import choose_browser, initialize_driver

def main():
    '''
    Main function to initialize the WebDriver and run the scraper.
    - Chooses a browser based on user input.
    - Initializes the WebDriver for the selected browser.
    - Calls the run_scraper function to execute the scraping process.
    '''
    driver = None
    try:
        browser = choose_browser()
        if browser is None:
            raise ValueError("No valid browser selected.")

        driver = initialize_driver(browser)
        if driver is None:
            raise WebDriverException("Failed to initialize WebDriver.")

        run_scraper(driver)

    except ValueError as e:
        print(f"Error: {e}")  # Log the specific error message
    except WebDriverException as e:
        print(f"WebDriver error: {e}")  # Log WebDriver specific error
    finally:
        if driver:
            driver.quit()
                
if __name__ == "__main__":
    main()
