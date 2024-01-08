import os
import json
import socket
from pprint import pprint
from html import unescape
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Blueprint

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        # absolute_path = f'{os.getcwd()}/web/session/session.json'
        history = request.args.get('history', 'normal').lower()
        with open('web/session/session.json', 'r+', encoding='utf-8') as f:
            get_sion = f.read()
            get_sion_list = json.loads(get_sion) if get_sion else []
        if history == 'all':
            ret_sion_list = get_sion_list
        else:
            ret_sion_list = get_sion_list[-10:]
        for i in range(0, len(ret_sion_list)):
            ret_sion_list[i]['text'] = unescape(ret_sion_list[i]['text'])
        context = {
            "get_sion_list": ret_sion_list
        }
        # pprint(context)
        return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
