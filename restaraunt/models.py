# -*-coding: utf-8 -*-
from django.db import models
from django.utils import timezone


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
    price = models.IntegerField(default=100, null=False, blank=False)

    class Meta:
        verbose_name = u'Блюдо'
        verbose_name_plural = u'Блюда'

    def __str__(self):
        return self.name.encode('utf-8')

class Storage(models.Model):
    date = models.DateField(default=timezone.now, null=False, blank=False)
    count = models.IntegerField(default=None, null=False, blank=False)
    expiration_date = models.DateField(default=None, null=True, blank=False)
    ingredient = models.ForeignKey(Ingredient)

    class Meta:
        verbose_name = u'Ячейка'
        verbose_name_plural = u'Склад'

    def __str__(self):
        return self.ingredient.name.encode('utf-8')

class Consist(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    count = models.IntegerField(default=1, null=False, blank=False)

    class Meta:
        verbose_name = u'Состоит'
        verbose_name_plural = u'Состав блюд'

    def __str__(self):
        return self.dish.name.encode('utf-8')


class Order(models.Model):
    dish = models.ForeignKey(Dish)
    date = models.DateField(default=timezone.now, null=False, blank=False)

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

    def __str__(self):
        return self.dish.name.encode('utf-8')

