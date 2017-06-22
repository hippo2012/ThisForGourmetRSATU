# -*- coding: utf-8 -*-

from . import views
from django.conf.urls import include, url, patterns

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^order/$', views.OrderView.as_view(), name='order')
]