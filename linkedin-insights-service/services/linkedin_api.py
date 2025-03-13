import requests
import os

LINKEDIN_API_URL = ""


class LinkedInAPI:
    def __init__(self):
        self.access_token = os.getenv("LINKEDIN_API_KEY")
        if not self.access_token:
            raise ValueError("Missing LinkedIn API Key. Set 'LINKEDIN_API_KEY' in the environment variables.")

    def get_page_data(self, page_id: str) -> dict:
        """Fetch LinkedIn organization (page) data by ID."""
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(f"{LINKEDIN_API_URL}/{page_id}", headers=headers)

        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch page data, status code: {response.status_code}", "details": response.text}

    def get_page_id(self, vanity_name: str) -> str:
        """Retrieve LinkedIn page ID using its vanity name."""
        url = f"{LINKEDIN_API_URL}?q=vanityName&vanityName={vanity_name}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get("elements", [])
            if data:
                return data[0].get("id")
            return "Page ID not found"
        return f"Error fetching page ID, status code: {response.status_code}"

# Example usage:
# api = LinkedInAPI()
# page_id = api.get_page_id("deepsolv")
# print(api.get_page_data(page_id))
