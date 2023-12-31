# src/retry_data.py
from pathlib import Path
from scraper import retry_failed_bibs
from utils import choose_browser

def main():
    '''
    Main function to retry scraping for failed attempts.
    It reads an error log to determine which entries need to be reprocessed and attempts to scrape them again.
    '''
    error_log_path = Path('logs/data_error.log')
    
    if not error_log_path.exists() or error_log_path.stat().st_size == 0:
        print("No failed data scraping records found.")
        return

    driver = None
    driver = choose_browser()
    retry_failed_bibs(driver, error_log_path)
    if driver:
        driver.quit()

if __name__ == "__main__":
    main()
