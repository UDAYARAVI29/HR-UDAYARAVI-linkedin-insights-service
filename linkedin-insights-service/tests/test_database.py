import unittest
from database import SessionLocal
from database import crud

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = SessionLocal()

    def test_create_page(self):
        data = {"page_id": "test123", "page_name": "Test Page", "followers": "10K"}
        page = crud.create_page(self.db, data)
        self.assertEqual(page.page_id, "test123")

if __name__ == "__main__":
    unittest.main()
