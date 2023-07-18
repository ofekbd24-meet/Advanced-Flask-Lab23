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
    "https://i.imgur.com/1dSgGnG.png": "The cohort of 2022!",
    "https://i.imgur.com/CPEvMk0.jpg": "MEET graduation!",
    "https://i.imgur.com/Cb7LK9o.jpg": "#MEET_HACKATHON",
    "https://i.imgur.com/S5A93Wt.jpg": "Class of 2024's Y1 closing event cohort"
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
