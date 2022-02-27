from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission


class IsTeacherOrDean(BasePermission):
    """
    Allows access to Teacher or Dean.
    """

    def has_permission(self, request, view):
        if request.user == AnonymousUser:
            return False
        return bool(request.user.status == "TEACHER" or request.user.status == "DEAN")
