
import requests
from parser import parse_product_details
from bs4 import BeautifulSoup

def parse_product_details(html_content, url):
    """Parse product details based on the URL structure."""
    soup = BeautifulSoup(html_content, 'html.parser')
    products = []
    
    # Example parsing logic for an Amazon-like website
    if "amazon.com" in url:
        product_elements = soup.select('.s-result-item')  # Example selector for product items
        for element in product_elements:
            product = {
                'name': element.select_one('h2 .a-link-normal').get_text(strip=True),  # Adjust as needed
                'price_gbp': element.select_one('.a-price .a-price-whole').get_text(strip=True),  # Adjust as needed
                'price_usd': element.select_one('.a-price .a-price-symbol').get_text(strip=True) + element.select_one('.a-price .a-price-whole').get_text(strip=True),  # Adjust as needed
                'price_kes': 'N/A',  # Set to 'N/A' or implement logic to fetch in KES if needed
            }
            products.append(product)

    elif "ebay.com" in url:
        product_elements = soup.select('.s-item')  # Example selector for eBay product items
        for element in product_elements:
            product = {
                'name': element.select_one('.s-item__title').get_text(strip=True),  # Adjust as needed
                'price_gbp': element.select_one('.s-item__price').get_text(strip=True),  # Adjust as needed
                'price_usd': 'N/A',  # Set to 'N/A' or implement logic to fetch in USD if needed
                'price_kes': 'N/A',  # Set to 'N/A' or implement logic to fetch in KES if needed
            }
            products.append(product)

    # Additional conditions for other websites can be added here...

    return products

# Function to scrape products from a given URL.
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

# added the input tag
if __name__ == "__main__":
    url = input("http://books.toscrape.com/catalogue/category/books_1")  # Replace with your target URL
    products = scrape_products(url)
    print(products)