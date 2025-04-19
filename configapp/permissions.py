from rest_framework.permissions import BasePermission

class IsAdminUserOnly(BasePermission):
    """
    Bu permission faqat admin foydalanuvchilarga ruxsat beradi.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_admin
