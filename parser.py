from bs4 import BeautifulSoup

def parse_product_details(html_content, url):
    """Parse the HTML content and extract product details from Books to Scrape."""
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Find all product containers
    product_containers = soup.find_all('article', class_='product_pod')
    
    products = []
    conversion_rate = 150  # Update this with the current KES to USD conversion rate
    gbp_to_usd_rate = 1.36  # Example conversion rate from GBP to USD, verify the current rate

    for container in product_containers:
        # Extract the product name
        product_name = container.h3.a['title'] if container.h3.a else 'No Name'
        
        # Extract the product price
        product_price_gbp = container.find('p', class_='price_color').text.strip()
        
        # Print the raw price for debugging
        print(f"Raw price string: '{product_price_gbp}'")
        
        # Clean the GBP price string
        clean_price = product_price_gbp.replace('£', '').replace(',', '').replace('Â', '').replace('\u00A0', '').strip()  # Remove unwanted characters
        
        try:
            # Convert the GBP price to a float
            product_price_gbp_value = float(clean_price)  # Clean GBP string
            
            # Convert GBP to USD
            product_price_usd = round(product_price_gbp_value * gbp_to_usd_rate, 2)  # Convert to USD

            # Optionally convert USD to KES if needed
            product_price_kes = round(product_price_usd * conversion_rate, 2)  # Convert USD to KES
            
            # Extract availability
            product_availability = container.find('p', class_='instock availability').text.strip() if container.find('p', class_='instock availability') else 'No Availability'
            
            # Append the product details to the list
            products.append({
                'name': product_name,
                'price_gbp': product_price_gbp,  # Price in GBP
                'price_usd': f"${product_price_usd}",  # Formatted price in USD
                'price_kes': f"KSh {product_price_kes}",  # Formatted price in KES
                'availability': product_availability
            })
        
        except ValueError as e:
            print(f"Error converting price: '{clean_price}', error: {e}")
    
    return products
