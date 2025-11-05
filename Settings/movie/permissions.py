from rest_framework.permissions import BasePermission, SAFE_METHODS

class GuestRestrictedPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        if getattr(user, 'status', None) != 'Guest':
            return True

        try:
            model_name = view.get_queryset().model.__name__
        except Exception:
            return True

        restricted_models = ['Actor', 'MovieLanguage']
        if model_name in restricted_models:
            return False

        if model_name == 'Movie':
            return request.method in SAFE_METHODS
        return True