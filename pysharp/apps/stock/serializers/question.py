# coding:utf-8
from rest_framework import serializers

from .base import ListSerializer


class QuestionListCommandSerializer(ListSerializer):
    keyword = serializers.CharField(required=False, default='')
    sorttype = serializers.CharField(required=False, default='')
    sortno = serializers.CharField(required=False, default='')


QUESTION_MODE = (
    ('free', '免费'),
    ('push', '系统推送'),
    ('onetoone', '一对一')
)


class QuestionCommandSerializer(serializers.Serializer):
    userid = serializers.CharField()
    content = serializers.CharField()
    questionmode = serializers.ChoiceField(choices=QUESTION_MODE)
    questionrelate = serializers.CharField(max_length=20)
    respondentid = serializers.CharField(required=False, default='')
    question_price = serializers.DecimalField(required=False, max_digits=18, decimal_places=2, default=0)
