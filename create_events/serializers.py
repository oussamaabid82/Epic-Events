from rest_framework.serializers import ModelSerializer
from django.db.models import Q

from authentication.serializers import UserSerializer
from authentication.models import User_crm
from create_events.models import Client, Contract, Event


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobil',
            'company_name',
            'address',
            'date_create'
        ]


class ClientDetailSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobil',
            'company_name',
            'address',
            'date_create',
            'sales_contact',
            'type',            
        ]
        depth = 1


class ContractListSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'signature_date',
            'event_name',
            'client',
            'start_date_event',
            'end_date_event',
            'amount',
            'payement_due',
        ]


class ContractDetailSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'signature_date',
            'event_name',
            'client',
            'sales_contact',
            'start_date_event',
            'end_date_event',
            'amount',
            'payement_due',
        ]
        depth = 2

class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'client',
            'start_date',
            'end_date',
            'support_contact',
        ]
   

class EventDetailSerializer(ModelSerializer):

    support_contact = UserSerializer
    print
    
    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'client',
            'start_date',
            'end_date',
            'support_contact',
            'contract',
            'note',
        ]
        depth = 3

class EventDetailSalesSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'client',
            'start_date',
            'end_date',
            'contract',
            'note',
        ]
        depth = 3
