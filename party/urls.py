from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls import handler404, handler500

urlpatterns = [
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('',views.index, name="index"),
    
]

handler404 = 'party.views.handler404'
handler500 = 'party.views.handler500'
handler403 = 'party.views.handler403'
