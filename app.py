from flask import Flask, render_template, Markup
from data import Topics
from flask_mysqldb import MySQL

app = Flask(__name__)


# init MySQL
mysql = MySQL(app)

Topics = Topics()

@app.route("/")
def home():
    return render_template('home.html', topics = Topics)

@app.route("/home/<string:id>/")
def lessons(id):

    return render_template('article.html', lessons = Topics[int(id)]['lessons'], topics = Topics)

@app.route("/books")
def books():
    return render_template('books.html')

if __name__ == "__main__":
    app.run()
