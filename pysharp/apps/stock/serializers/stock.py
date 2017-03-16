# coding:utf-8
from rest_framework import serializers


class StockCommandSerializer(serializers.Serializer):
    keyword = serializers.CharField(required=False, default='')
    sorttype = serializers.CharField(required=False, default='')
    sortno = serializers.CharField(required=False, default='')
    pindex = serializers.IntegerField()
    psize = serializers.IntegerField()


class StockSerializer(serializers.Serializer):
    stockname = serializers.CharField()
    stockcode = serializers.CharField()
    lastprice = serializers.FloatField()
    prevclose = serializers.FloatField()
    open = serializers.FloatField()
    changeamount = serializers.FloatField()
    changerate = serializers.FloatField()
    highest = serializers.FloatField()
    lowest = serializers.FloatField()
    tradingvolume = serializers.FloatField()
    changingover = serializers.FloatField()
    turnoverrate = serializers.FloatField()
    peratio = serializers.FloatField()
    circulatecap = serializers.FloatField()
    totalcap = serializers.FloatField()
    pbratio = serializers.FloatField()
