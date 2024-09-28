
import requests
from bs4 import BeautifulSoup
from parser import parse_product_details
from storage import save_to_csv

def fetch_page(url):
    """Fetch the HTML content of the webpage."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")

def main():
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'  # Update this URL as needed
    html_content = fetch_page(url)
    
    # Parse the content and extract data
    products = parse_product_details(html_content)
    
    # Save data to CSV
    save_to_csv(products, 'products.csv')  # Save as products.csv or any preferred name

if __name__ == "__main__":
    main()