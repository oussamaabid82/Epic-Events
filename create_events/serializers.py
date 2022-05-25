from rest_framework.serializers import ModelSerializer
from django.db.models import Q

from authentication.serializers import UserSerializer
from authentication.models import User_crm
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
            'type',
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

    # user = User_crm.objects.filter(team='SUPPORT')
    
    # print(user)
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
        depth = 3