from django.db import models

class Message_recv(models.Model):
    time_recv=models.DateTimeField(auto_now_add=True)
    message_recv=models.TextField(max_length=50)
    view=models.IntegerField(default=0)

    class Meta:
        ordering=['-time_recv']
    def	__str__(self):
        return "{0}/{1}/{2}\n".format(self.id,self.time_recv.strftime('%B %d, %Y, %I:%M %p'),self.message_recv)


class Message_send(models.Model):
    time_send=models.DateTimeField(auto_now=True)
    cmd=models.TextField(max_length=50,null=True)
    camera=models.TextField(max_length=10,null=True)
    message_send=models.TextField(max_length=150,null=True)
    def	__str__(self):
        return "{0}/{1}/{2}/{3}\n".format(self.time_send,self.cmd,self.camera,self.message_send)
