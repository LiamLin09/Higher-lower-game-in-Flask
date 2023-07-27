from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home_page():
    return "<h1>Guess number between 0 and 9.</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'> "


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return '<h1 style="color:purple">YOUR GUESS IS TOO HIGH, TRY AGAIN!!!!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    elif guess < random_number:
        return '<h1 style="color:red">YOUR GUESS IS TOO LOW, TRY AGAIN!!!!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    else:
        return '<h1 style="color:green">YOU FOUND ME!!!!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
