from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .serializers import RecvSerializer,SendSerializer
from messageapp.models import Message_recv,Message_send

class MessageRecvList(generics.ListCreateAPIView):
    queryset=Message_recv.objects.all()
    serializer_class=RecvSerializer

class MessageRecvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Message_recv.objects.all()
    serializer_class=RecvSerializer

class MessageSendList(generics.ListCreateAPIView):
    queryset=Message_send.objects.all()
    serializer_class=SendSerializer

class MessageSendDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Message_send.objects.all()
    serializer_class=SendSerializer
