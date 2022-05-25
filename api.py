import flask
from flask import request, jsonify
import sqlite3


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():

    return '''<h1>API</h1>
<p>Esta API retorna dados do Sqlite.</p>'''


@app.route('/dicionario', methods=['GET'])
def api_all():
     conn = sqlite3.connect('example.db')
     cur = conn.cursor()

     all_books = cur.execute('SELECT * FROM APIIEEE').fetchall()

     # for row in cur.execute('SELECT * FROM APIEEE'):
     #     print(row)
     return jsonify(all_books)


app.run()
