import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class LinkedInScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def scrape_page(self, page_id: str) -> dict:
        url = f"https://www.linkedin.com/company/{page_id}/"
        self.driver.get(url)
        time.sleep(5)  # Allow time for page to load

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        page_data = {
            "page_id": page_id,
            "page_name": self._get_text(soup, "h1"),
            "description": self._get_text(soup, "p"),
            "followers": self._extract_followers(soup),
            "profile_picture": self._extract_profile_picture(soup),
            "industry": self._extract_industry(soup),
        }
        self.driver.quit()
        return page_data

    def _get_text(self, soup, tag):
        element = soup.find(tag)
        return element.text.strip() if element else None

    def _extract_followers(self, soup):
        span = soup.find("span", text=lambda t: "followers" in t.lower())
        return span.text.strip() if span else "N/A"

    def _extract_profile_picture(self, soup):
        img = soup.find("img", {"alt": "Company Logo"})
        return img["src"] if img else None

    def _extract_industry(self, soup):
        span = soup.find("span", text=lambda t: "Industry" in t)
        return span.text.strip() if span else None

# Example usage:
# scraper = LinkedInScraper()
# print(scraper.scrape_page("deepsolv"))
