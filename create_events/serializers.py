from datetime import datetime
from django.forms import ValidationError
from rest_framework.serializers import ModelSerializer

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
            'date_create',
            'sales_contact',
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

    def validate(self, data):

        USER_DATETIME = datetime.now().strftime("%Y-%m-%d")

        start_date = data['start_date_event']
        end_date = data['end_date_event']
        amount = data['amount']

        if USER_DATETIME > str(start_date):
            raise ValidationError('Vérifiez la date de debut')

        if str(start_date) > str(end_date):
            raise ValidationError('Vérifiez la date de la fin')

        if amount < 0:
            raise ValidationError('Le montant dois etre positif')

        return data


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

    def validate(self, data):

        USER_DATETIME = datetime.now().strftime("%Y-%m-%d")

        start_date = data['start_date_event']
        end_date = data['end_date_event']
        amount = data['amount']

        if USER_DATETIME > str(start_date):
            raise ValidationError('Vérifiez la date de debut')

        if str(start_date) > str(end_date):
            raise ValidationError('Vérifiez la date de la fin')

        if amount < 0:
            raise ValidationError('Le montant dois etre positif')

        return data


class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'statu',
            'event_name',
            'client',
            'start_date',
            'end_date',
            'support_contact',
            'note',
        ]


class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'statu',
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
            'statu',
            'event_name',
            'client',
            'start_date',
            'end_date',
            'contract',
            'note',
        ]
        depth = 3
