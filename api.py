import flask
from flask import request, jsonify
import sqlite3
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    
    return '''<h1>API</h1>
<p>Esta API retorna dados do Sqlite.</p>'''
app.run()


@app.route('/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('exemple.db')
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM APIEEE;').fetchall()

    return jsonify(all_books)



