# books/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a staff user for write operations,
    or is a safe method (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        # Allow read-only requests for any authenticated user
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Write requests only if user is staff
        return bool(request.user and request.user.is_staff)
