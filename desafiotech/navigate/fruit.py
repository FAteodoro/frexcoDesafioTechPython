from rest_framework import viewsets
from desafiotech.models import Fruit
from desafiotech.navigate import serializers


class FruitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FruitSerializer
    queryset = Fruit.objects.all()
