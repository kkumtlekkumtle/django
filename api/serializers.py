from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Mera:
        model = Item
        fields = ("__all__")
        