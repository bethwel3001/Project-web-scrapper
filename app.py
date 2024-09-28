
from flask import Flask, render_template, request
from scrapper import scrape_products

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    products = scrape_products(url)
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

# 
