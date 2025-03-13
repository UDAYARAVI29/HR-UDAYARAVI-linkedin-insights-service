import unittest
from services.scraper import LinkedInScraper

class TestLinkedInScraper(unittest.TestCase):
    def test_scrape_page(self):
        scraper = LinkedInScraper()
        data = scraper.scrape_page("linkedin")

        self.assertIn("page_name", data)
        self.assertIn("followers", data)
        self.assertIsInstance(data, dict)

if __name__ == "__main__":
    unittest.main()
