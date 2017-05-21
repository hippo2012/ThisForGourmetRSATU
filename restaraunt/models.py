from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=False)

class Dish(models.Model):
    name=models.CharField(max_length=255, default='', null=False, blank=False)
    ingredient = models.ManyToManyField(Ingredient)
