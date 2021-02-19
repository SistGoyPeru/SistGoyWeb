from django.http import request
from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail

# CREANDO LAS VISTAS

def inicio(request):
    if request.method=="POST":
        subject=request.POST['asunto']
        message=request.POST['mensaje']+" "+request.POST['email']
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['alexgoyzueta2018@gmail.com']
        send_mail(subject,message,email_from,recipient_list)

    return render(request,'sistgoyapp/index.html')

