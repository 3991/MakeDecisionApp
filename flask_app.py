from flask import Flask, render_template, Markup, abort
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)
app.config["DEBUG"] = True

"""SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{hostname}/{databasename}".format(
    username="charlemagneIsAlr",
    password="sdfghjkl",
    hostname="charlemagneIsAlreadyTaken.mysql.pythonanywhere-services.com",
    databasename="charlemagneIsAlr$flask_note",
)
"""
SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="sdfgh",
    hostname="localhost",
    databasename="flaskDB",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    theme_id = db.Column(db.Integer, db.ForeignKey('theme.id'))

class Lesson(db.Model):
    __tablename__ = "lessons"
    id = db.Column(db.Integer, primary_key=True)
    lesson = db.Column('lesson', db.Unicode)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))

class Source(db.Model):
    __tablename__ = "sources"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    author = db.Column('author', db.Unicode)

class Theme(db.Model):
    __tablename__ = "themes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)


tags = Tag.query.all()

@app.route("/")
def home():
    try:
        themes = Theme.query.all()
        if not themes:
            abort(404)
        return render_template('home.html', themes = themes)
    except Exception as e:
        return render_template('home.html', error = e)

@app.route("/home/tags/<string:theme_id>/")
def tags(theme_id):
    try:
        themes = Theme.query.all()
        tags = Tag.query.filter_by(theme_id=theme_id).all()
        if not themes or not tags:
            abort(404)
        return render_template('home.html', themes = themes, tags = tags, theme_id = theme_id)
    except Exception as e:
        return render_template('home.html', error = e)

@app.route("/home/lessons/<string:tag_id>/<string:theme_id>/")
def lesson(tag_id, theme_id):
    try:
        themes = Theme.query.all()
        tags = Tag.query.filter_by(theme_id=theme_id).all()
        lessons = Lesson.query.filter_by(tag_id=tag_id).all()
        sources = Source.query.all()
        if not themes or not tags or not lessons or not sources:
            abort(404)
        return render_template('home.html', themes = themes, tags = tags, lessons = lessons, sources = sources, theme_id = theme_id)
    except Exception as e:
        print(e)
        return render_template('home.html', error = e)

# permanent link
@app.route("/perm/<string:lesson_id>/<string:tag_id>/<string:theme_id>/")
def permanent_link(lesson_id, tag_id, theme_id):
    try:
        lesson = Lesson.query.filter_by(id=lesson_id).first()
        tag = Tag.query.filter_by(theme_id=theme_id).first()
        theme = Theme.query.filter_by(id=theme_id).first()
        sources = Source.query.all()
        if not lesson or not sources:
            abort(404)
        return render_template('permanent.html', tag = tag, lesson = lesson, sources = sources, tag_id = tag_id, theme_id = theme_id, theme = theme)
    except Exception as e:
        return render_template('permanent.html', error = e)


"""@app.route("/home/<string:id>/")
def lessons(id):
    try:
        sources = Source.query.all()
        lessons = Lesson.query.filter_by(tag_id=id).all()
        tag = Tag.query.filter_by(id=id).first()
        theme = Theme.query.filter_by(id=tag.theme_id).first()
        return render_template('article.html', tags = tags, tag = tag, theme = theme, lessons = lessons, sources = sources)
    except Exception as e:
        print(e)

@app.route("/theme/<string:id>/")
def themes(id):
    try:
        theme = Theme.query.filter_by(id=id).first()
        tag = Tag.query.filter_by(theme_id=id).first()
        sources = Source.query.all()
        lessons = Lesson.query.filter_by(tag_id=tag.id).all()

        return render_template('themes2.html', theme = theme, tag = tag, lessons = lessons, sources = sources)
    except Exception as e:
        print(e)
"""

@app.route("/sources")
def books():
    try:
        sources = Source.query.all()
        if not sources:
            abort(404)
        return render_template('sources.html', sources = sources)
    except Exception as e:
        print(e)

@app.route("/about")
def about():
    try:
        return render_template('about.html')
    except Exception as e:
        return render_template('about.html', error = e)

@app.route("/news")
def news():
    try:
        return render_template('news.html')
    except Exception as e:
        return render_template('news.html', error = e)

@app.route("/random")
def random():
    random = randint(1,40)
    try:
        lesson = Lesson.query.filter_by(id=random).first()
        sources = Source.query.all()
        tag = Tag.query.filter_by(id=lesson.tag_id).first()
        return render_template('random.html', lesson = lesson, sources = sources, tag = tag)
    except Exception as e:
        return render_template('random.html', error = e)


@app.route("/error")
def error():
    return render_template('error.html')
"""
@app.route("/themes")
def theme():
    try:
        themes = Theme.query.all()
        tags = Tag.query.all()
        if not themes:
            abort(404)
        return render_template('themes.html', themes = themes, tags = tags)
    except Exception as e:
        print(e)
"""
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404


if __name__ == "__main__":
    app.run()
