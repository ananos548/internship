from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import News, InvestmentProject
from .serializers import NewsSerializers, InvestmentProjectSerializers


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class InvestmentProjectViewSet(ModelViewSet):
    queryset = InvestmentProject.objects.all()
    serializer_class = InvestmentProjectSerializers
