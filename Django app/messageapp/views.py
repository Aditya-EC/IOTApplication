from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Message_recv,Message_send
from django.urls import reverse_lazy
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.template import loader
import asyncio

import requests as rq


global dt
global var
var=''
global load
load=0

class Message(ListView):
    model=Message_recv
    template_name='message.html'

class Doc(TemplateView):
    template_name='documentation.html'

class Dashboard(TemplateView):
    template_name='serial.html'

class Video(TemplateView):
    template_name='video.html'

class Contact(TemplateView):
    template_name='contacts.html'

class About(TemplateView):
    template_name='about.html'
    

class MessageListView(ListView):
    model=Message_recv
    #template_name=''

class MessageCreateView(CreateView):
    model=Message_send
    #template_name=''
    fields='__all__'

class MessageUpdateView(UpdateView):
    model=Message_send
    #template_name=''
    fields=['time','cmd','message']

class MessageCameraView(UpdateView):
    model=Message_send
    #template_name=''
    fields=['camera']

class MessageDeleteView(DeleteView):
    model=Message_recv
    template_name='new.html'
    success_url = reverse_lazy('message')


def new_value(request):
    nm=Message_recv.objects.filter(view=0)
    var=''
    for i in nm:
        var+=str(i)+"~"
    for i in nm:
        i.view=1
        i.save()
    return HttpResponse(var)

def message(request):
    zvm=Message_recv.objects.filter(view=0)
    for i in zvm:
        i.view=1
        i.save()
    return HttpResponse('done')

def change_camera(request):
    global load
    chc=Message_send.objects.filter(id=10)
    for i in chc:
        if(i.camera=='OFF'):
            i.camera='ON'
            i.save()
            return HttpResponse("camera is on")
        else:
            i.camera='OFF'
            i.save()
            load=0
            return HttpResponse("camera is off")

def camera_status(request):
    global load
    chc=Message_send.objects.filter(id=10)
    if(chc[0].camera=='OFF'):
        return HttpResponse("OFF")
    else:
        return HttpResponse("ON")
        
def camera_loading(request):
    global laod
    ct=datetime.now()
    i=0
    while(i<10):
        async def main():
            await asyncio.sleep(1)
        asyncio.run(main())
        var1=Message_send.objects.filter(id=10)
        msgtime1=var1[0].time_send
        msg=var1[0].message_send
        if((ct < msgtime1) and (msg=='Camera On')):
            break
        i+=1
    else:
        chc=Message_send.objects.filter(id=10)
        for i in chc:
            if(i.camera=='On'):
                i.camera='OFF'
                i.save()
        return HttpResponse('error')
    load=1
    chc=Message_send.objects.filter(id=10)
    for i in chc:
        i.message_send='OK'
        i.save()
    return HttpResponse('done')
    
    
        

def command(request,cmd):
    msg=Message_send.objects.filter(id=10)
    
    pl=dict(cm=cmd)
    purl='http://c9e1394f.ngrok.io/api'
    lurl='http://127.0.0.1:5000/api'
    r=rq.post(purl,data=pl)
    
    
    for i in msg:
        i.cmd=cmd
        i.save()
    ct=datetime.now()
    async def main():
        global var
        await asyncio.sleep(4)
        var=Message_send.objects.filter(id=10)
    asyncio.run(main())
    
    mt=var[0].time_send
    if(mt>ct):
        return HttpResponse(var[0].message_send)
    else:
        return HttpResponse('ERROR : Device not connected')






