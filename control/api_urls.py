# -*- coding: utf-8 -*-

from . import api as views
from django.conf.urls import include, url, patterns

urlpatterns = [
    url(r'^dish/$', views.Dish.as_view(), name='dish_add'),
    url(r'^dish/(?P<id>\d+)/$', views.Dish.as_view(), name='dish'),
    url(r'^ingredient/$', views.Ingredient.as_view(), name='ingredient_add'),
    url(r'^ingredient/(?P<id>\d+)/$', views.Ingredient.as_view(), name='ingredient'),
    url(r'^menu_export/$', views.menu_export, name='menu_export'),
    url(r'^ingredients_export/$', views.ingredients_export, name='ingredients_export')
]