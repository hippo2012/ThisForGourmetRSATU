# -*- coding: utf-8 -*-

from . import api as views
from django.conf.urls import include, url, patterns

urlpatterns = [
    url(r'^dish/$', views.Dish.as_view(), name='dish')
]