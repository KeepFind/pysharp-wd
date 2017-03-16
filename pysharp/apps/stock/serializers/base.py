#coding:utf-8
from rest_framework import serializers

class ListSerializer(serializers.Serializer):
    pindex=serializers.IntegerField()
    psize=serializers.IntegerField()