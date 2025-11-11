from rest_framework import permissions 


class EventHostPermissions(permissions.BasePermission):
    """
    Permission to check if the user is an event host.

    This permission grants access only to users who have the 'event_hoster'
    flag set to True.
    """

    def has_permission(self, request, view):
        """
        Checks if the user is an event host.

        Args:
            request (Request): The request object.
            view (View): The view being accessed.

        Returns:
            bool: True if the user is an event host, False otherwise.
        """
        if request.user.event_hoster:
            return True
        return False


class EventHostOrReadOnly(permissions.BasePermission):
    """
    Permission to allow read-only access for anyone, but write access
    only to the event host or admin users.
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if the user has permission to perform the action on the object.

        Allows safe methods (GET, HEAD, OPTIONS) for all users.
        Allows all methods for staff users.
        Allows all methods if the user is the host of the event object.

        Args:
            request (Request): The request object.
            view (View): The view being accessed.
            obj (object): The object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

        return request.user == obj.host


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to allow read-only access for anyone, but write access
    only to admin users.
    """

    def has_permission(self, request, view):
        """
        Checks if the user has permission for the view.

        Allows safe methods for all users.
        Allows all methods only for staff (admin) users.

        Args:
            request (Request): The request object.
            view (View): The view being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff 