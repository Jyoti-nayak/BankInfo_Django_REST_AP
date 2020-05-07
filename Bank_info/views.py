from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class BankList(APIView):
    def get(self,request):
        model = Bank_info.objects.all()
        serializer = BankInfoSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BankInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BankDetails(APIView):
    def get(self,request, city):
        try:
            model = Bank_info.objects.get(id=city)
        except Bank_info.DoesNotExist:
            return Response(f"City {city} not found in DB", status=status.HTTP_404_NOT_FOUND)
        serializer = BankInfoSerializer(model)
        return Response(serializer.data)

    def put(self,request,city):
        try:
            model = Bank_info.objects.get(id=city)
        except Bank_info.DoesNotExist:
            return Response(f"City {city} not found in DB", status=status.HTTP_404_NOT_FOUND)
        serializer = BankInfoSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,city):
        try:
            model = Bank_info.objects.get(id=city)
        except Bank_info.DoesNotExist:
            return Response(f"City {city} not found in DB", status=status.HTTP_404_NOT_FOUND)
        serializer = BankInfoSerializer(model)
        model.delete()
        return Response(f"City {city} deleted from DB", status=status.HTTP_204_NO_CONTENT)
