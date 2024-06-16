from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# Generate the right random number
right_number = random.randint(1, 9)

@app.route('/')
def hello_world():
    return render_template_string('''
        <h1 style="text-align: center">Welcome to my World!</h1>
        <p style="text-align: center">Now Choose a number between 1 to 9</p>
        <img style="display: block; margin: auto;" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeG9vaDZrb21ydmVkOHZjMDU3ZGxxMGh1dzluYjJ3YWZlYTN4MHBiMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/t9Xb7Kgdvdf2SETVjf/giphy.gif" width="500">
        <form style="text-align: center" method="POST" action="/submit">
            <input type="number" name="number" min="1" max="9">
            <button type="submit">Submit</button>
        </form>
    ''')

@app.route('/submit', methods=['POST'])
def submit_number():
    user_number = int(request.form['number'])
    
    # Check if the number is correct
    if user_number > right_number:
        return render_template_string('''
            <h1 style='color: purple; text-align: center'>Too high, try again!</h1>
            <img style="display: block; margin: auto;" src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHl1aGd4em11NXJobml5ZnlycmJodHoyem4yemhpejBwMmlrczNnYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fQoIDlLW6A6BAhyev8/giphy.gif'/>
            <a href="/" style="display: block; text-align: center">Try Again</a>
        ''')
    elif user_number < right_number:
        return render_template_string('''
            <h1 style='color: red; text-align: center'>Too low, try again!</h1>
            <img style="display: block; margin: auto;" src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW45YnNyZ3hka2pleTgwOXAzdXY1cmU1eGltcWp3bjFpM2hpc2EzMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dGjy2bjeSfbc3WQBRX/giphy.gif'/>
            <a href="/" style="display: block; text-align: center">Try Again</a>
        ''')
    else:
        return render_template_string('''
            <h1 style='color: green; text-align: center'>You found me!</h1>
            <img style="display: block; margin: auto;" src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnQwajB6ZGxpMW85bnA5MWFybWtoaXR1cnpoZWE4aHMzbGQ1cHE1ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d3mlE7uhX8KFgEmY/giphy.gif'/>
            <a href="/" style="display: block; text-align: center">Play Again</a>
        ''')

if __name__ == "__main__":
    app.run(debug=True)
