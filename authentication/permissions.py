from rest_framework.permissions import BasePermission
from . models import User_crm


class IsManager(BasePermission):
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)