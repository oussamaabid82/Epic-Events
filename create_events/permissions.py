from rest_framework.permissions import BasePermission
from django.db.models import Q
from authentication.models import User_crm
from create_events.models import Contributor


class IsClientManager(BasePermission):

    def has_permission(self, request, view):

        SALES_GRANTED_METHOD = ('GET', 'POST', 'PUT')
        SUPPORT_GRANTED_METHOD = ('GET')

        try:
            user = Contributor.objects.get(
                Q(client_id=view.kwargs['id']) & Q(user=request.user.username))
            print(user)

            if request.user.is_authenticated and request.user.is_superuser:
                return True
            
            if request.user.team == 'management':
                return True

            if request.user.is_authenticated and request.user.team == 'SALES' and request.method in SALES_GRANTED_METHOD:
                return True

            if request.user.is_authenticated and user.team == 'SUPPORT' and request.method in SUPPORT_GRANTED_METHOD:
                return True

        except Exception:
            print ("Vous n'êtes pas autorisé")
