# coding:utf-8

from flask import Flask, jsonify, request

# 请求方式错误
method_err = {
    "code": 301,
    "msg": "请求方式错误，只支持POST请求"
}
# 参数错误
param_err = {
    "code": 302,
    "msg": "请求参数错误，请检查入参"
}
# 成功信息
success_msg = {
    "code": 200,
    "msg": "调用成功"
}

# 这个是初始化一个服务，__name__代表是咱们写的这个python文件,
# 也就是咱们这个python文件就是一个服务了，然后赋值给app，app就代表这个服务了
app = Flask(__name__)


@app.route('/test', methods=['POST', 'GET'])
#路径为/test，方法为post和get
def test():
    if request.method != 'POST':#判断是否post方法
        return jsonify(method_err)
    else:
        user_id = request.values.get("user_id")
        print(user_id)
        if user_id=='aaa':
            return jsonify(success_msg)
        else:
            return jsonify(param_err)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001, debug=True)#运行的地址 和端口，debug是否打开
