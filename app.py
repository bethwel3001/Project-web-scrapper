
from flask import Flask, render_template, request
from scrapper import scrape_products
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/scrap')
def scrap():
    return render_template('index.html')

@app.route('/know-more')
def know_more():
    return render_template('know_more.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    products = scrape_products(url)
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

