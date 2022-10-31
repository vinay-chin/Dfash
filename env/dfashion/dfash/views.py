import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import Contact
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name,email=email,subject=subject,msg=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'index.html')