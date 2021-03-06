"""
  Created by kebo on 2018/6/22
"""
from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'OK'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we make a mistake! '
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found 0__0...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'

class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'
