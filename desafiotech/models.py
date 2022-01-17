from django.db import models


class Region(models.Model):
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.region


class Fruit(models.Model):
    fruit = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.Region
