from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from create_events.permissions import IsClientManager, IsContractManager, IsEventManager
from . models import Client, Contract, Event
from . serializers import (
    ClientListSerializer, ClientDetailSerializer, ContractDetailSerializer,
    ContractListSerializer, EventDetailSalesSerializer, EventDetailSerializer,
    EventListSerializer
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
    permission_classes = [IsClientManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'email']

    def get_queryset(self):

        user = self.request.user

        if user.team == 'management':
            return Client.objects.all()

        elif user.team == 'sales':
            return Client.objects.filter(sales_contact=user)

        event = Event.objects.get(support_contact=user)
        if user.team == 'support':
            return Client.objects.filter(id=event.client.id)

        raise PermissionDenied

    def perform_create(self, serializer):
        # l'utilsateur connecter c'est l'agent commercial qui a contacter le client
        commercial_agent = serializer.save(sales_contact=self.request.user)
        client_type = serializer.save(type='client_potentiel')


class ContractViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsContractManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__last_name', 'client__email', 'signature_date', 'amount']

    def get_queryset(self):

        user = self.request.user

        if user.team == 'management':
            return Contract.objects.all()

        if user.team == 'sales':
            return Contract.objects.filter(sales_contact=user)

        raise PermissionDenied

    def perform_create(self, serializer):

        contact = serializer.save(sales_contact=self.request.user, status=True)

        # recupération des données pour ensuite crééer un événement
        name = self.request.data.get('event_name')
        start_date = self.request.data.get('start_date_event')
        end_date = self.request.data.get('end_date_event')
        serializer.save()
        contract = self.get_queryset().last()
        client = (Client.objects.filter(id=contract.client.id)[0])

        Event.objects.create(
            event_name=name,
            client=client,
            start_date=start_date,
            end_date=end_date,
            contract=contract,
            statu='a_venir'
        )

        # Mettre à jour le type de client
        client_existant = Client.objects.filter(id=contract.client.id).update(type='client_existant')


class EventViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    detail_serializer_class_sales = EventDetailSalesSerializer
    permission_classes = [IsEventManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__last_name', 'client__email', 'start_date']

    def get_queryset(self):

        # Afficher les evenements liéer au contrat
        return Event.objects.filter(contract_id=self.kwargs['contract_pk'])

    def get_serializer_class(self):

        user = self.request.user

        if user.team == 'management':
            if self.action == 'retrieve':
                return self.detail_serializer_class
            return super().get_serializer_class()

        if user.team == 'sales':
            if self.action == 'update':
                return self.detail_serializer_class_sales
            return super().get_serializer_class()

        if user.team == 'support':
            if self.action == 'update':
                return self.detail_serializer_class_sales
            return super().get_serializer_class()


class EventsListViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    detail_serializer_class_sales = EventDetailSalesSerializer
    permission_classes = [IsEventManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__last_name', 'client__email', 'start_date']

    def get_queryset(self):
        user = self.request.user

        if user.team == 'management':
            # Afficher tous evenements pour tous les utilisateurs de l'équipe management
            return Event.objects.all()

        elif user.team == 'support':
            # Afficher les événements liéer à l'utilisateur de l'équipe support
            return Event.objects.filter(support_contact=user)

        raise PermissionDenied

    def perform_create(self, serializer):

        print(serializer)

    def get_serializer_class(self):

        user = self.request.user

        if user.team == 'management':
            if self.action == 'retrieve':
                return self.detail_serializer_class
            return super().get_serializer_class()

        # if user.team == 'sales':
        #     if self.action == 'update':
        #         return self.detail_serializer_class_sales
        #     return super().get_serializer_class()

        if user.team == 'support':
            if self.action == 'update':
                return self.detail_serializer_class_sales
            return super().get_serializer_class()
