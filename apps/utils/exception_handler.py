"""
错误消息处理
"""

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        data = {"status_code": response.status_code}
        if "detail" not in response.data:
            data["message"] = response.data
        else:
            data["message"] = response.data["detail"]

        response.data = data

    return response
