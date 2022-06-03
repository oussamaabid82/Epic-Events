from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException

from authentication.models import User_crm


class IsClientManager(BasePermission):

    def has_permission(self, request, view):

        SALES_GRANTED_METHOD = ('GET', 'POST', 'PUT')
        SUPPORT_GRANTED_METHOD = ('GET')

        try:
            user = User_crm.objects.get(username=request.user.username)

            if request.user.is_authenticated and request.user.is_superuser:
                return True

            if request.user.is_authenticated and user.team == 'management':
                return True

            if request.user.is_authenticated and user.team == 'sales' and request.method in SALES_GRANTED_METHOD:
                return True

            if request.user.is_authenticated and user.team == 'support' and request.method in SUPPORT_GRANTED_METHOD:
                return True

        except User_crm.DoesNotExist:
            raise APIException('You are not allowed.')


class IsContractManager(BasePermission):

    def has_permission(self, request, view):

        SALES_GRANTED_METHOD = ('GET', 'POST')
        SUPPORT_GRANTED_METHOD = ('GET')

        try:
            user = User_crm.objects.get(username=request.user.username)

            if request.user.is_authenticated and request.user.is_superuser:
                return True

            if request.user.is_authenticated and user.team == 'management':
                return True

            if request.user.is_authenticated and user.team == 'sales' and request.method in SALES_GRANTED_METHOD:
                return True

            if request.user.is_authenticated and user.team == 'support' and request.method in SUPPORT_GRANTED_METHOD:
                return True

        except User_crm.DoesNotExist:
            raise APIException('You are not allowed.')


class IsEventManager(BasePermission):

    def has_permission(self, request, view):

        GRANTED_METHOD = ('GET', 'PUT')

        try:
            user = User_crm.objects.get(username=request.user.username)

            if request.user.is_authenticated and request.user.is_superuser:
                return True

            if request.user.is_authenticated and user.team == 'management' and request.method in GRANTED_METHOD:
                return True

            if request.user.is_authenticated and user.team == 'sales' and request.method in GRANTED_METHOD:
                return True

            if request.user.is_authenticated and user.team == 'support' and request.method in GRANTED_METHOD:
                return True

        except User_crm.DoesNotExist:
            raise APIException('You are not allowed.')
