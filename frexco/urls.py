from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from desafiotech.navigate import fruit, region

route = routers.DefaultRouter()
route.register(r"region", region.RegionViewSet)
route.register(r'fruit', fruit.FruitViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
