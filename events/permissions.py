from rest_framework.permissions import BasePermission, SAFE_METHODS

class Is_organizer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'organizer'

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.organizer == request.user

class Is_confirmed_attendee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.registrations.filter(user=request.user, status='confirmed').exists()