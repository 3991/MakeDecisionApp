from flask import Flask, render_template, Markup, abort
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
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))

class Source(db.Model):
    __tablename__ = "sources"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    author = db.Column('author', db.Unicode)

class Theme(db.Model):
    __tablename__ = "themes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)

class Theme_Tags(db.Model):
    __tablename__ = "themes_tags"
    id = db.Column(db.Integer, primary_key=True)
    theme_id = db.Column(db.Integer, db.ForeignKey('theme.id'))
    tag_name = db.Column('tag_name', db.Unicode)


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
        sources = Source.query.all()
        lessons = Lesson.query.filter_by(tag_id=id).all()
        return render_template('article.html', tags = tags, lessons = lessons, sources = sources)
    except Exception as e:
        print(e)

@app.route("/books")
def books():
    try:
        sources = Source.query.all()
        return render_template('books.html', sources = sources)
    except Exception as e:
        print(e)

@app.route("/error")
def error():
    return render_template('error.html')

@app.route("/themes")
def theme():
    try:
        themes = Theme.query.all()
        themes_tags = Theme_Tags.query.all()
        if not themes:
            abort(404)
        return render_template('themes.html', themes = themes, themes_tags = themes_tags)
    except Exception as e:
        print(e)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    app.run()
