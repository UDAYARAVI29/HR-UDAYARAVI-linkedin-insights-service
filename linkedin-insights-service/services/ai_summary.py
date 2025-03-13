import google.generativeai as genai
import os

class AISummary:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    def generate_summary(self, text: str) -> str:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(text)
        return response.text if response and hasattr(response, 'text') else "Error generating summary"

# Example usage:
# ai = AISummary()
# print(ai.generate_summary("This page has 50k followers and specializes in AI."))
