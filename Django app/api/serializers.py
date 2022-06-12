from rest_framework import serializers
from messageapp.models import Message_recv,Message_send

class RecvSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message_recv
        fields='__all__'

class SendSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message_send
        fields='__all__'
