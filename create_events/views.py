from rest_framework.viewsets import ModelViewSet
from . models import Client, Contract, Event, Contributor
from . serializers import (
    ClientListSerializer, ClientDetailSerializer, 
    ContractSerializer, EventListSerializer, 
    EventDetailSerializer, ContributorSerializer
)


class ClientViewSet(ModelViewSet):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    
    def get_queryset(self):
        return Client.object.all()
    

class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    
    def get_queryset(self):
        return Contract.object.all()


class EventViewSet(ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    
    def get_queryset(self):
        return Event.object.all()
    
    
class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    
    def get_queryset(self):
        return Contributor.objects.all()