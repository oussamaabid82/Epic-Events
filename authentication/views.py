from rest_framework.viewsets import ModelViewSet

from .models import User_crm
from .serializers import UserSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User_crm.objects.all()


class SignupViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return[]

