from django.shortcuts import render

from django.http import HttpResponse
from django.core.mail import send_mail

from app1.forms import *
# Create your views here.
def Registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            

            NSPO=PFD.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()

            send_mail('Registration','user registration Sucessfully','achyuthsiddha43@gmail.com',[NSUO.email],fail_silently=True)






            return HttpResponse(' data is Successfully inserted:')
        



    return render(request,'Registration.html',d)