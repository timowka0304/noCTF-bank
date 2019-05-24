#!/usr/bin/python3
from flask import Flask, render_template, request, g, jsonify, redirect, make_response
import sqlite3, os

app = Flask(__name__)
app.database = "sample.db"

def connect_db():
    return sqlite3.connect(app.database)


@app.route('/<owner>', methods=['GET'])
def search(owner):
    g.db = connect_db()
    curs = g.db.execute("SELECT * FROM history WHERE owner=?", (owner,)) 
    results = [dict(owner=row[0], balance=row[1], target=row[2], transfer_id=row[3]) for row in curs.fetchall()]
    g.db.close()
    return jsonify(results)


if __name__=='__main__':
    app.run(host='127.0.0.1', port=9090)