from django.shortcuts import render
from rest_framework import status
# Create your views here.

from rest_framework.views import APIView
from ticket.models import Ticket
from Api.serializers import Tktserializer
from rest_framework.response import Response
# Create your views here.
class TktList(APIView):
    def get(self,request):
        books=Ticket.objects.all()
        serializer=Tktserializer(books,many=True)
        return Response(serializer.data)   

class Createtkt(APIView):
    def post(self,request):
        serializer=Tktserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    