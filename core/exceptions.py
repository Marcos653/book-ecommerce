from rest_framework.exceptions import APIException
from django.utils.translation import ugettext as _
from rest_framework.exceptions import APIException, _get_error_details
from rest_framework import status


class ForgotPasswordExpired(APIException):
    status_code = 404
    default_detail = _('Link expirado')
    default_code = 'permission_denied'

class InvalidPassword(APIException):
    status_code = 404
    default_detail = _('Senha inválida')
    default_code = 'permission_denied'

class ForgotPasswordInvalidParams(APIException):
    status_code = 404
    default_detail = _('Parametros inválidos')
    default_code = 'permission_denied'


class UserDoesNotExist(APIException):
    status_code = 404
    default_detail = _('Usuário não existe')
    default_code = 'permission_denied'   


class SocialNetworkError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

    def __init__(self, detail=None, code=None, status_code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code
        if status_code is not None:
            self.status_code = status_code

        self.detail = _get_error_details(detail, code)