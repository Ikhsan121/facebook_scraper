import pickle
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import undetected_chromedriver as uc
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Load environment variables from the .env file
load_dotenv()

# Access variables
username = os.getenv("PHONE_NUMBER")
password = os.getenv("PASSWORD")


def initialize_browser():

    # Automatically download and use the correct version of ChromeDriver
    # Configure Chrome options
    options = uc.ChromeOptions()
    # block pop-up notification
    prefs = {
    "profile.default_content_setting_values.notifications": 2  # 2 means block
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--lang=en-US")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

    #  initialize WebDriver
    driver = uc.Chrome(options=options)

    return driver


def login(driver):
    # Wait for the login page
    driver.get('https://www.facebook.com/')
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
    except Exception as e:
        print(f"Error: {e}")
        return

    # Locate elements and send keys
    try:
        username_bar = driver.find_element(By.ID, 'email')
        username_bar.send_keys(username)

        password_bar = driver.find_element(By.ID, 'pass')
        password_bar.send_keys(password)

        login_button = driver.find_element(By.NAME, 'login')
        login_button.click()
    except Exception as e:
        print(f"Error during login: {e}")


def save_cookies(driver):
    login(driver)
    # Save cookies to a file
    cookies = driver.get_cookies()
    with open("cookies.pkl", "wb") as file:
        pickle.dump(cookies, file)

    print("Cookies have been saved!")


def load_cookies(driver):
    driver.get('https://www.facebook.com/')
    # Load cookies from the file
    with open("cookies.pkl", "rb") as file:
        cookies = pickle.load(file)

    # Add cookies to the browser
    for cookie in cookies:
        # Skip adding the "expiry" field if present (not required for set_cookie)
        cookie.pop("expiry", None)
        driver.add_cookie(cookie)

    # Reload the webpage to apply cookies
    driver.refresh()

    print("Cookies have been loaded and applied!")
    sleep(1)

