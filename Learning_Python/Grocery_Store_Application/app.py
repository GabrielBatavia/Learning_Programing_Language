# .\env\Scripts\activate


from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new/')
def new_orders():
    return render_template('new_orders.html')

@app.route('/manage/')
def manage():
    return render_template('manage_product.html')

if __name__ == "__main__":
    app.run(debug=True)