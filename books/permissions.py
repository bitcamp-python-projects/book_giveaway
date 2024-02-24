from rest_framework import permissions

class IsOwnerOrStaffForPatch(permissions.BasePermission):
    """
    wishlistis permission nebas rTavs path requesti gamogzavnos mxolod adminebma da wignis mflobelebma.
    """

    def has_permission(self, request, view):
        # Check if the request method is PATCH
        if request.method == 'PATCH':
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # 
        return obj.book.owner == request.user or request.user.is_staff

class WishListPermission(permissions.BasePermission):
    """
    Wishlist permission
    """

    def has_permission(self, request, view):
        # Only authenticates users can send POST request 
        if request.method == 'POST':
            return request.user.is_authenticated
        
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        print(obj)
        # Admins can everything 
        if user.role == 'administrator':
            return True

        # Only owners can add SUBMIT status 
        if user.role == 'owner':
            if request.method in permissions.SAFE_METHODS:
                return True  # Allows read-only actions
            return obj.user == user and obj.status == 'pending'

        # Disrupts access for everyone
        return False
