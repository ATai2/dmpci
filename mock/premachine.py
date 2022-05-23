
import os
from flask import Flask, request, redirect, url_for, send_from_directory, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)


# user = {"userName": "admin", "password": "admin"}

# 前置机mock

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/nofile")
def nofile():
    rsp = make_response("{}")
    rsp.headers['Content-Type'] = 'text/plain'
    return rsp


@app.route("/xccj/services/fileUpload", methods=["POST", "GET"])
def fileUpload():
    # a=request.form
    mark = request.args.get('REPAIRMARK')
    user = request.args.get('USER')
    pwd = request.args.get('PASSWORD')

    if mark is None:
        return {"serviceFlag": "0", "msg": "无mark"}

    if user is None:
        return {"serviceFlag": "0", "msg": "无user"}

    if pwd is None:
        return {"serviceFlag": "0", "msg": "无pwd"}

    if 'file' not in request.files:
        # flash('No file part')
        return {"serviceFlag": "0", "msg": "file"}
    file = request.files['file']
    # 如果用户没有选择文件
    # 浏览器也会提交没有文件名的空部分
    if file.filename == '':
        # flash('No selected file')
        return {"serviceFlag": "0", "msg": "无file"}
    if file:
        filename = file.filename
        path = os.path.join(os.path.abspath('.'), "dir")
        exists = os.path.exists(path)
        if not exists:
            os.makedirs(path)
        file.save(os.path.join(path, filename))
    return {"serviceFlag": "1", "msg": "ok"}


@app.route("/xccj/services/tempDownload", methods=["POST", "GET"])
def tempDownload():
    bustype = request.args.get('BUSTYPE')
    user = request.args.get('USER')
    pwd = request.args.get('PASSWORD')

    if bustype is None:
        return {"serviceFlag": "0", "msg": "无bustype"}

    if user is None:
        return {"serviceFlag": "0", "msg": "无user"}

    if pwd is None:
        return {"serviceFlag": "0", "msg": "无pwd"}

    noRes = {"serviceFlag": "0", "msg": "下载接口:没有 新文件"}

    path = os.path.join(os.path.abspath('.'), "temp", bustype)
    exists = os.path.exists(path)
    if not exists:
        os.makedirs(path)

    filename = ""
    for item in os.listdir(path):
        print(item)
        filename = item
        break

    return send_from_directory(path, filename, as_attachment=True)
    # return {"serviceFlag": "1", "msg": "ok"}


@app.route("/xccj/services/logDownload", methods=["POST", "GET"])
def logDownload():
    return {"serviceFlag": "1", "msg": "ok"}


@app.route("/xccj/services/fileFeedbackDownload", methods=["POST", "GET"])
def fileFeedbackDownload():
    return {"serviceFlag": "1", "msg": "ok"}


@app.route("/xccj/services/realTimeQuery", methods=["POST", "GET"])
def realTimeQuery():
    return {"serviceFlag": "1", "msg": "ok"}


@app.route("/xccj/services/realTimeFileUpload", methods=["POST", "GET"])
def realTimeFileUpload():
    return {"serviceFlag": "1", "msg": "ok"}


if __name__ == '__main__':
    # 在IP 地址127.0.0.1 的8000 端口运行应用程序
    app.run(host='0.0.0.0', port=9500, debug=True)
