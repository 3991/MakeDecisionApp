from flask import Flask, render_template, Markup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True


app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Tag(db.Model):

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)

class Lesson(db.Model):

    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)
    lesson = db.Column('lesson', db.Unicode)
    source = db.Column('source', db.Unicode)
    tag_id = db.Column('tag_id', db.Integer)
tags = Tag.query.all()
@app.route("/")
def home():
    try:
        return render_template('home.html', tags = tags)
    except Exception as e:
        return render_template('home.html', error = e)

@app.route("/home/<string:id>/")
def lessons(id):
    try:
        lessons = Lesson.query.filter_by(tag_id=id).all()
        print(id)
        print(lessons)
        return render_template('article.html', tags = tags, lessons = lessons)
    except Exception as e:
        print("error")

@app.route("/books")
def books():
    return render_template('books.html')

if __name__ == "__main__":
    app.run()
