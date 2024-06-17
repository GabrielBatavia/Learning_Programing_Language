from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_number():
    user_name = request.form.get('text')
    API_KEY = f"https://api.genderize.io?name={user_name}"
    gender_response = requests.get(API_KEY).json()
    gender = gender_response.get('gender')
    probability = gender_response.get('probability')
    return render_template('submit.html', gender=gender, probability=probability) 


@app.route('/Blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url).json()
    return render_template('blog.html', posts=response)
        

if __name__ == "__main__":
    app.run(debug=True)