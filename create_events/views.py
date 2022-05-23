from operator import contains
from tkinter import Entry
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from . models import Client, Contract, Event, Contributor
from . serializers import (
    ClientListSerializer, ClientDetailSerializer, ContractSerializer, 
    EventListSerializer, EventDetailSerializer, ContributorSerializer
)


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ClientViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer

    def get_queryset(self):
        return Client.objects.all()

    def perform_create(self, serializer):
        # l'utilsateur connecter c'est l'agent commercial qui a contacter le client 
        client = serializer.save(contact_by=self.request.user)


class ContractViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ContractSerializer
    
    def get_queryset(self):
        return Contract.objects.all()


    def perform_create(self, serializer):
        # recupération des données pour ensuite crééer un événement
        name = self.request.data.get('event_name')
        start_date = self.request.data.get('start_date_event')
        end_date = self.request.data.get('end_date_event')
        serializer.save()
        contract = self.get_queryset().last()

        Event.objects.create(
            event_name=name,
            start_date=start_date,
            end_date=end_date,
            contract=contract
        )


class EventViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()
