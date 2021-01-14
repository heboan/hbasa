from django.http import JsonResponse


class StatusCode():
    ok = 200
    params_error = 400
    un_auth = 401
    method_error = 405
    server_error = 500


def result(code, message, data):
    return JsonResponse({"code": code, "message":message, "data":data or {}})


def success(message='', data=None):
    return result(code=StatusCode.ok, message=message, data=data)


def params_error(message='', data=None):
    """ 请求参数错误 """
    return result(code=StatusCode.params_error, message=message, data=data)


def unauth_error(message='', data=None):
    """ 没有权限访问 """
    return result(code=StatusCode.un_auth, message=message, data=data)


def method_error(message='', data=None):
    """ 请求方法错误 """
    return result(code=StatusCode.method_error, message=message, data=data)


def server_error(message='', data=None):
    """ 服务器内部错误 """
    return result(code=StatusCode.server_error, message=message, data=data)