from flask import render_template
from app import app
from .data_importer import extracted_data


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', data=extracted_data)


@app.route('/books')
def books():
    return render_template('books.html', title='Books')


@app.route('/authors')
def authors():
    return render_template('authors.html', title='Authors')