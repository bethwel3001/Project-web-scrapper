
import requests
from parser import parse_product_details
from bs4 import BeautifulSoup
# Function to scrape products from a given URL.
def scrape_products(url):
    """Scrapes products from the provided URL and returns a list of products."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        html_content = response.content
        products = parse_product_details(html_content, url)
        return products
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
# added the input tag
if __name__ == "__main__":
    url = input("http://books.toscrape.com/catalogue/category/books_1")  # Replace with your target URL
    products = scrape_products(url)
    print(products)