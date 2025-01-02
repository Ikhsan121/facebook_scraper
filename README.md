# **Facebook Profile Data Scraper**

A Python-based web scraping tool to automate the extraction of detailed profile information from Facebook. This project uses Selenium with undetected ChromeDriver to handle dynamic web content and bypass bot detection.

---

## **Features**

- **Profile Data Extraction**:
  - Scrapes names, contact info, gender, relationship status, work details, education history, and hometown.
- **Cookie Handling**:
  - Automates login with saved cookies for seamless scraping.
- **Dynamic Content Support**:
  - Handles JavaScript-rendered pages with Selenium.
- **Headless Mode**:
  - Operates in the background without opening a browser window.
- **CSV Output**:
  - Saves the extracted data into a structured CSV file.

---

## **Technologies Used**

- **Python 3.10**: Core programming language.
- **Selenium**: Web automation tool for handling dynamic content.
- **Undetected ChromeDriver**: Bypasses bot detection mechanisms.
- **Pandas**: Processes and organizes extracted data.
- **Environment Variables**: Manages credentials securely using `.env` files.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ikhsan121/facebook_scraper.git
   cd facebook_scraper
   ```
2.Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4.Set Up Environment Variables: Configure your credentials for login by creating a .env file in the root directory. Add the following variables:
```makefile
PHONE_NUMBER=your_phone_number
PASSWORD=your_password
```

