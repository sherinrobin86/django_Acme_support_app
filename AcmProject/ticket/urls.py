
from ticket.views import tkt_details,tkt_add
from django.urls import path
app_name='ticket'
urlpatterns = [
     path("tkt/",tkt_details,name='tktdetails'),
     path('tkt/add/',tkt_add,name='tkt_add'),
] 