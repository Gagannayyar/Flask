import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = False

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=["GET"])
def home():
    return "<h1>Test Flask API</h1><p>Just testing how flask API works</p>"


@app.route('/api/v1/resources/books/all', methods=["GET"])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute("SELECT * FROM books;").fetchall()

    return jsonify(all_books)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource code could not be found</p>", 404

@app.route('/api/v1/resources/books', methods=["GET"])
def api_filter():
    query_parameter = request.args

    id = query_parameter.get('id')
    published = query_parameter.get('published')
    author = query_parameter.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    print(query)

    query = query[:-4] + ';'

    print(query)
    print(to_filter)

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query,to_filter).fetchall()

    return jsonify(results)




app.run()
