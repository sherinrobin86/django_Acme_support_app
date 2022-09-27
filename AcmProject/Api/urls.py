from django.contrib import admin
from django.urls import path
from Api.views import  TktList,Createtkt

urlpatterns = [
    path("list/",TktList.as_view()),
    path('create/',Createtkt.as_view()),
   
]
