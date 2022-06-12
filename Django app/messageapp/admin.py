from django.contrib import admin
from .models import Message_recv,Message_send

admin.site.register(Message_recv)
admin.site.register(Message_send)
