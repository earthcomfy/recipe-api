from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Check if authenticated user is author of the recipe.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated is True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
