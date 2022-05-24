from rest_framework.serializers import ModelSerializer
from create_events.models import Client, Contract, Event, Contributor


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'company_name',
            'address',
            'phone_number',
            'email',
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
            'client_type',
        ]
        depth = 1


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'signature_date',
            'event_name',
            'client',
            'start_date_event',
            'end_date_event',
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
        ]
        depth = 3


class ContributorListSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
        ]
        

class ContributorDetailSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
            'client',
            'event',
        ]
