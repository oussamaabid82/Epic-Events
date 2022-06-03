from rest_framework.permissions import BasePermission


class IsManager(BasePermission):

    def has_permission(self, request, view):

        try:

            if request.user.is_authenticated and request.user.is_superuser:
                return True

            if request.user.team == 'management':
                return True

        except Exception:
            print("Vous n'êtes pas autorisé")
