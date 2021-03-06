from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Return the username property if not return get the User instance then return username
        try:
            print(obj.username)
            return obj.username == request.user.username
        except AttributeError as err:
            return obj.user.username == request.user.username
