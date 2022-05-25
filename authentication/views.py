from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from authentication.permissions import IsManager

from .models import User_crm
from .serializers import UserSerializer


class UserViewset(ReadOnlyModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User_crm.objects.all()


class SignupViewset(ModelViewSet):
    permission_classes = [IsManager]
    serializer_class = UserSerializer

    def get_queryset(self):
        return[]

