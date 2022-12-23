from rest_framework.exceptions import APIException

class LoginFailed(APIException):
    status_code = 400
    default_detail = "Login failed, invalid credentials"
    default_code = "Login failed"

class UserExists(APIException):
    status_code = 403
    default_detail = "user already exists"
    default_code = "registration failed"

class UserNotFound(APIException):
    status_code = 404
    default_detail = "User not found"
    default_code = "User not found"