import os
import json
import socket
from pprint import pprint
from html import unescape
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Blueprint, session


app = Flask(__name__)
app.secret_key = 'NSAO@0)@*jsjsj*@(EjsakKskdd2340202'


# @app.route('/')
# @app.route('/test', methods=['GET', 'POST'])
# def test():
#     if request.method == 'GET':
#         return render_template('test.html')


# @app.route('/')
@app.route('/<key_name>', methods=['GET', 'POST'])
def hello_world(key_name):
    with open('web/session/secure_chars', 'r+', encoding='utf-8') as f:
        g_secure_chars = f.read()
    if request.method == 'GET' and key_name != '' and key_name == g_secure_chars:
        session['username'] = 'admin'
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
    else:
        return render_template('404.html')


@app.route('/upload_video', methods=['POST'])
def file_receive():
    if request.method == 'POST' and 'username' in session.keys() and session['username'] == 'admin':
        # 获取文件对象
        file = request.files.get('videoFile')
        if not file:
            return {'code': 400, 'message': '未接收到文件'}
        # filename = file.filename.replace(" ", "")
        filename = file.filename
        save_path = os.path.join('web/static/upload/video', filename)
        file.save(save_path)    # 保存文件

        # 如果需要获取额外参数，可用 request.form 或 request.data
        # extra_info = request.form.get('info')
        print(filename)
        return {
            'code': 200,
            'message': '文件上传成功',
            'fileName': filename
        }
    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
