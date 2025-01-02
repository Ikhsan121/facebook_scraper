import csv
from time import sleep
import pandas as pd
from scraper.web_scraper import initialize_browser, login, save_cookies, load_cookies
from selenium.webdriver.common.by import By
from scraper.data_getter import user_info
import random
import os


def load_csv():
    # Read the CSV file
    df = pd.read_csv('test_url.csv')
    profile_address = df['username link']

    return profile_address


def process(drv) -> None:
    links = load_csv()
    final_data = []


    load_cookies(drv)  # Load cookies once if applicable

    for link in links:
        drv.get(link)
        final_data.append(user_info(drv, link))
        sleep(1)
    drv.quit()

    # Write to CSV
    csv_file = "output.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=final_data[0].keys())
        writer.writeheader()  # Write the header
        writer.writerows(final_data)  # Write the data rows

    print(f"Data written to {csv_file}")


if __name__ == "__main__":
    file_path = "cookies.pkl"
    # Check if the cookies exists
    if os.path.exists(file_path):
        print(f"The file '{file_path}' exists.")
        process(initialize_browser())
    else:
        print(f"The file '{file_path}' does not exist.")
        print("Login and save cookies.")
        driver = initialize_browser()
        login(driver)
        save_cookies(driver)
        process(drv=driver)



