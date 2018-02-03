from flask import Flask, render_template, Markup
from data import Topics
from flask_mysqldb import MySQL

app = Flask(__name__)



# init MySQL
mysql = MySQL(app)

Topics = Topics()

@app.route("/")
def home():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM tags")
    tags = cur.fetchall()
    cur.close()
    if result > 0:
        return render_template('home.html', tags = tags)
    else:
        error = 'Tags not found'
        return render_template('home.html', error = error)

@app.route("/home/<string:id>/")
def lessons(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM tags")
    tags = cur.fetchall()
    result2 = cur.execute("SELECT * FROM lessons WHERE tag_id = %s", [id])
    lessons = cur.fetchall()
    cur.close()
    if result > 0:
        return render_template('article.html', tags = tags, lessons = lessons)
    else:
        error = 'Tags not found'
        return render_template('article.html', error = error)


@app.route("/books")
def books():
    return render_template('books.html')

if __name__ == "__main__":
    app.run()
