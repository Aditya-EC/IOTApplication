from django.urls import path
from .views import Message,Dashboard,Video,Contact,About,Doc,MessageDeleteView
from. import views

urlpatterns=[path('',Message.as_view(),name='message'),
             path('m/<int:pk>/delete/',MessageDeleteView.as_view(),name='mess'),
             path('documentation/',Doc.as_view(),name='doc'),
             path('serial/',Dashboard.as_view(),name='serial'),
             path('video/',Video.as_view(),name='video'),
             path('contact/',Contact.as_view(),name='contact'),
             path('about/',About.as_view(),name='about'),
             path('messagefunc',views.message,name='messagefunc'),
             path('newmessages/',views.new_value,name='newmessage'),
             path('change_camera/',views.change_camera,name='change_camera'),
             path('camera_status/',views.camera_status,name='camera_status'),
             path('camera_loading/',views.camera_loading,name='camera_loading'),
             path('cmd_message/<path:cmd>',views.command,name='commands'),
             
            ]
