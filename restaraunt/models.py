# -*-coding: utf-8 -*-
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=False)

    class Meta:
        verbose_name = u'Ингредиент'
        verbose_name_plural = u'Ингредиенты'

    def __str__(self):
        return self.name.encode('utf-8')


class Dish(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=False)
    ingredient = models.ManyToManyField(Ingredient)

    class Meta:
        verbose_name = u'Блюдо'
        verbose_name_plural = u'Блюда'

    def __str__(self):
        return self.name.encode('utf-8')
