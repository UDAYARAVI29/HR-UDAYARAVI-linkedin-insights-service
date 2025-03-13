import subprocess

def run_spiders():
    print("Running LinkedIn Page Scraper...")
    subprocess.run(["scrapy", "crawl", "linkedin_page", "-o", "output/pages.json"])

    print("Running LinkedIn Posts Scraper...")
    subprocess.run(["scrapy", "crawl", "linkedin_posts", "-o", "output/posts.json"])

    print("Scraping complete. Data saved in the 'output' folder.")

if __name__ == "__main__":
    run_spiders()
