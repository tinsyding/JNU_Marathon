
# src/retry_data.py
from selenium.common.exceptions import WebDriverException
from scraper import retry_failed_bibs
from utils import initialize_driver, choose_browser
from pathlib import Path

def main():
    '''
    Main function to retry scraping for failed attempts.
    It reads an error log to determine which entries need to be reprocessed and attempts to scrape them again.
    '''
    error_log_path = Path('logs/data_error.log')
    
    # Check if there are any failed records to retry
    if not error_log_path.exists() or error_log_path.stat().st_size == 0:
        print("No failed data scraping records found.")
        return

    driver = None
    try:
        browser = choose_browser()
        if browser is None:
            raise ValueError("No valid browser selected.")

        driver = initialize_driver(browser)
        retry_failed_bibs(driver, error_log_path)
    except WebDriverException as e:
        print(f"Web driver error: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()