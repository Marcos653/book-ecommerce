from rest_framework import permissions
from rest_framework.response import Response

SAFE_METHODS = ['POST']


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, iew):
        if request.method in SAFE_METHODS:
            return True
        if request.method == "GET":
            return True
        if request.method == "PATCH":
            return request.user.is_authenticated
        else:
            return request.user.is_admin