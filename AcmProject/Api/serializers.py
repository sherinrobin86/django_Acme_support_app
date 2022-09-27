from rest_framework import serializers
from ticket.models import Ticket

class Tktserializer(serializers.Serializer):
    subject=serializers.CharField()
    desc=serializers.CharField()
    priority=serializers.CharField()
    email=serializers.EmailField()
    phone=serializers.IntegerField()

    def create(self,data):
        return Ticket.objects.create(**data)