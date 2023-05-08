from django.shortcuts import render

from django.http import HttpResponse
from django.core.mail import send_mail

from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

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


def Home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'Home.html',d)
    return render(request,'Home.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('Home'))
        else:
            return HttpResponse("invalid username & Password")

    return render(request,'user_login.html')

@login_required
def User_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))

def Display_Profile(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'Display_Profile.html',d)

@login_required
def Change_Password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse("Password Sucessfully changed:")
        
    return render(request,'Change_Password.html')