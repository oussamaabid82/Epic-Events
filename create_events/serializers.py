
from attr import fields
from rest_framework.serializers import ModelSerializer
from create_events.models import Client, Contract, Event, Contributor


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'company_name',
            'contact_by',
        ]
        

class ClientDetailSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'company_name',
            'address',
            'phone_number',
            'email',
            'contact_by',
            'contributor',
        ]
        

class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'signature_date',
            'client',
            'event',
        ]


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'start_date',
            'end_date',
        ]


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'start_date',
            'end_date',
            'contract',
            'contributor',
        ]


class ContributorSerializer(ModelSerializer):
    
    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
            'client',
            'event',
        ]