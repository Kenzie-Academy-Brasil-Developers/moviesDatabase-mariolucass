from rest_framework import permissions
from rest_framework.views import Request, View


class AdminOrCriticPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and request.user.is_critic or request.user.is_superuser


class AdminPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and request.user.is_superuser


class AdminOrReadOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        is_safe_method = request.method in permissions.SAFE_METHODS
        return is_safe_method or request.user.is_authenticated and request.user.is_superuser


class AdminOrCriticOrReadOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        is_safe_method = request.method in permissions.SAFE_METHODS
        return is_safe_method or request.user.is_authenticated and (request.user.is_critic or request.user.is_superuser)
