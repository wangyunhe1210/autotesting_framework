# -*- coding:utf-8 -*-
from flask import Flask, request, Response, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/post_method_one', methods=['POST'])
def post_method_one():
    try:
        res = {'sum': request.json['first'] + request.json['second'], 'errorcode': 'success'}
        return jsonify(res)
    except Exception as e:
        res = {'errorcode': 'error'}
        return jsonify(res)


@app.route('/post_method_two', methods=['POST'])
def post_method_two():
    try:
        res = {'sum': int(request.form['first']) + int(request.form['second']), 'errorcode': 'success'}
        return jsonify(res)
    except Exception as e:
        res = {'errorcode': 'error'}
        return jsonify(res)


app.run(debug=True)
