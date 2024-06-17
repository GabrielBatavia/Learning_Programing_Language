from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    year1 = date.today().year
    return render_template('index.html', num=random_number, year=year1)


if __name__ == "__main__":
    app.run(debug=True)