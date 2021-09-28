from django.shortcuts import render, redirect
from .models import *

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def index(request):
    return render(request , 'other/contact.html')

def handler404(request, exception):
    return render(request, 'error/404.html')

def handler403(request, exception):
    return render(request, 'error/403.html')

def handler500(request):
    return render(request, 'error/500.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'authentication/login.html')
    else:
        username = request.POST['username']
        date = request.POST['date']
        password = "12345"
        fixedDate = "2019-03-02"
        # 2nd March 2019 - YES 
        if not fixedDate == date:
            messages.error(request, "Entered date is wrong.")
            return redirect('login')

        user = auth.authenticate(username=username, password=password)

        if user is not None:

            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Entered wrong username")
            return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('/')
