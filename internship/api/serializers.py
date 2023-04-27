# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import News, InvestmentProject


class NewsSerializers(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class InvestmentProjectSerializers(ModelSerializer):
    class Meta:
        model = InvestmentProject
        fields = '__all__'
