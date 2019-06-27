from charts.models import Stock
from charts.serializers import StockSerializer
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('date')
    serializer_class = StockSerializer
    # serializer.data


@csrf_exempt
def portfolio(request):
    queryset = Stock.objects.all().order_by('date')
    profit = 0
    min_num = 0
    max_num = 0
    for i in range(len(queryset) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if queryset[i].data - queryset[j].data > profit:
                profit = queryset[i].data - queryset[j].data
                max_num = i
                min_num = j
    return JsonResponse({
        'buy_date': queryset[min_num].date,
        'sell_date': queryset[max_num].date,
    })

#