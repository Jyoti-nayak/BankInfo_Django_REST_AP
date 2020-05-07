# api  <-->  mobile app/ web app etc. convert to JSON data

from rest_framework import serializers
from .models import Bank_info

class BankInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_info
        fields = '__all__'





