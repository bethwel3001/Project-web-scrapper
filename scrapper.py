
import requests
from parser import parse_product_details

def scrape_products(url):
    """Scrapes products from the provided URL and returns a list of products."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        html_content = response.content
        products = parse_product_details(html_content)
        return products
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
# Uncomment the following line to test scraping from a specific URL
# scrape_products("https://example.com/products")
if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"  # Replace with your target URL
    products = scrape_products(url)
    print(products)