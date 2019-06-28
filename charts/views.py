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
    profit, min_num, max_idx, min_idx = 0, 99999, 0, 0
    for idx, data in enumerate(queryset):
        if data.close_price < min_num:
            min_num = data.close_price
            min_idx = idx
        if data.close_price - min_num > profit:
            profit = data.close_price - min_num
            max_idx = idx

    return JsonResponse({
        'buy_date': queryset[min_idx].date,
        'sell_date': queryset[max_idx].date,
    })
