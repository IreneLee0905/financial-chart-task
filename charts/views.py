from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from charts.models import Stock
from charts.serializers import StockSerializer


# Create your views here.


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('date')
    serializer_class = StockSerializer
    # serializer.data

