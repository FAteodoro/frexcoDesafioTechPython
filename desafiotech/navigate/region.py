from rest_framework import viewsets
from desafiotech.models import Region
from desafiotech.navigate import serializers


class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegionSerializer
    queryset = Region.objects.all()

