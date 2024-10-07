Web Scraper
Overview
This project is a simple web scraper built in Python that extracts product details from a specified e-commerce website. The scraper fetches product names and prices, converts the prices from GBP to USD and KES, and stores the information in a CSV file.
![image](https://github.com/user-attachments/assets/4e286da7-ccd3-40e1-8797-fbdd25158ff3)

Features
Scrapes product information from a given URL.
For example https://www.jumia.co.ke/televisions/
Parses HTML content to extract product names and prices.
Converts prices from GBP to USD and KES.
Saves the scraped data into a CSV file.
Requirements
To run this project, you will need the following Python libraries:
![image](https://github.com/user-attachments/assets/e8165e84-3f1b-4c99-8f53-0b095bf9da1b)

requests
BeautifulSoup (from bs4)
You can install the required libraries using pip:
![image](https://github.com/user-attachments/assets/4bb6d4ef-cec3-41a9-b611-44420e285a80)

pip install requests beautifulsoup4

Project Structure
webscraper/
│
├── app.py          # Flask app for future frontend integration
├── scraper.py      # Main scraper logic
├── parser.py       # Parses HTML to extract product details
└── output.csv      # Output CSV file for scraped data (created upon running the scraper)

Usage
1.Set the Target URL: Open scraper.py and set the url variable to the target e-commerce site you want to scrape. Make sure to adjust the selectors in parser.py according to the website's structure.

2.Run the Scraper: Execute the following command in your terminal:
python scraper.py

3.Check the Output: After running the scraper, you should find an output.csv file in the project directory containing the scraped product information.

Example
Here is a simple example of how to use the scraper:
from scraper import scrape_products

url = " # Replace with your target URL" 
products = scrape_products(url)
print(products)  # Display the scraped product data

Notes
Be sure to check the website's robots.txt file to ensure that scraping is allowed.
Adjust the scraping logic in parser.py based on the actual HTML structure of the target website.
This scraper is designed for educational purposes and may require modifications for production use.
