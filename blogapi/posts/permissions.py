from rest_framework import permissions


# custom class extending BasePermission
class IsAuthorOrReadOnly(permissions.BasePermission):
    # override has_object_permission if http request contains SAFE_METHODS touple (read only)
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        # smart syntax, implicit elif, operator returns true or false
        return obj.author == request.user
