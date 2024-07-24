
from flask import Flask, render_template, request, send_from_directory
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/m')
def mobile():
    return render_template('mobile.html')


@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')


# Default port:
if __name__ == '__main__':
    app.run(port=os.getenv('PORT'))