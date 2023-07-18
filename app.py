from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://hips.hearstapps.com/hmg-prod/images/beautiful-smooth-haired-red-cat-lies-on-the-sofa-royalty-free-image-1678488026.jpg"

user_bio = "Middle East Entrepreneurs of Tomorrow. Enabling the next generation of Israeli and Palestinian leaders."

posts = {
    "https://images.saymedia-content.com/.image/t_share/MTk2NzY3MjA5ODc0MjY5ODI2/top-10-cutest-cat-photos-of-all-time.jpg": "Small cat",
    "https://t4.ftcdn.net/jpg/00/97/58/97/360_F_97589769_t45CqXyzjz0KXwoBZT9PRaWGHRk5hQqQ.jpg": "cat stare",
    "https://t4.ftcdn.net/jpg/03/03/62/45/360_F_303624505_u0bFT1Rnoj8CMUSs8wMCwoKlnWlh5Jiq.jpg": "cat sunglasses",
    "https://images.squarespace-cdn.com/content/v1/62a39d94533ec9640a7f1042/1673553575786-8ZNDZCSHQX6B14YHV8EF/fat+cat.jpg": "cute fat cat"
}

#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html', image_link=image_link, user_bio=user_bio, posts=posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
