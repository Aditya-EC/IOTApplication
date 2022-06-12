from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[path('v3.9/variables/values/recv/',views.MessageSendList.as_view()),
             path('v3.9/variables/values/recv/<int:pk>',views.MessageSendDetail.as_view()),
             path('v3.9/variables/values/send/',views.MessageRecvList.as_view()),
             path('v3.9/variables/values/send/<int:pk>',views.MessageRecvDetail.as_view()),
             ]

urlpatterns = format_suffix_patterns(urlpatterns)
