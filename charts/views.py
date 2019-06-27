from charts.models import Stock
from charts.serializers import StockSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Stock Restful API
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('date')
    serializer_class = StockSerializer


# Calculating best portfolio
@csrf_exempt
def portfolio(request):
    queryset = Stock.objects.all().order_by('date')
    profit, min_num, max_num = 0, 0, 0
    # Iterate and find the largest difference between two prices
    for i in range(len(queryset) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if queryset[i].close_price - queryset[j].close_price > profit:
                profit = queryset[i].close_price - queryset[j].close_price
                max_num = i
                min_num = j
    return JsonResponse({
        'buy_date': queryset[min_num].date,
        'sell_date': queryset[max_num].date,
    })
