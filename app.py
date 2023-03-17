from flask import Flask, render_template
from helper import pages, page_photo, page_blurb, page_logo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", pages=pages, page_photo=page_photo, page_blurb=page_blurb, page_logo=page_logo)


@app.route('/adventures')
def adventures():
    return render_template('adventures.html', pages=pages, page_photo=page_photo, page_logo=page_logo)

@app.route('/music')
def music():
    return render_template('music.html', pages=pages, page_photo=page_photo, page_logo=page_logo)

@app.route('/projects')
def projects():
    return render_template('projects.html', pages=pages, page_photo=page_photo, page_logo=page_logo)

@app.route('/about')
def about():
    return render_template('about.html', pages=pages, page_photo=page_photo, page_logo=page_logo)

