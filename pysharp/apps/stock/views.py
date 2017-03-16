from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from utils.response import retmsg
from .serializers.stock import StockCommandSerializer, StockSerializer
from .services.stock import StockService
from utils.decorators import request_validate
from .models import AppStock


class StockViewSet(viewsets.ModelViewSet):
    queryset = AppStock.objects.all()

    @list_route(url_path='getstocklist')
    @request_validate(StockCommandSerializer)
    def get_stocks(self, request, *args, **kwargs):
        '''
        获取股票列表
        '''

        stocks = StockService().get_stocks(**kwargs['command'])
        retmsg['data'] = StockSerializer(stocks, many=True).data

        return Response(retmsg)