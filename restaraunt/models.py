from django.db import models

class Dish(models.Model):
    name=models.CharField(max_length=255, default='', null=False, blank=False)
