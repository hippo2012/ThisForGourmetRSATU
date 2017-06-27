# -*- coding: utf-8 -*-

from . import api as views
from django.conf.urls import include, url, patterns

urlpatterns = [
    url(r'^dish_order/(?P<id>\d+)/$', views.DishOrder.as_view(), name='dish_order')
]