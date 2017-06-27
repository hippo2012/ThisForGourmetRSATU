# -*- coding: utf-8 -*-

from . import views
from django.conf.urls import include, url, patterns

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^ingredients/$', views.IngredientsView.as_view(), name='ingredients'),
    url(r'^orders/(?P<id>\d+)/$', views.OrdersView.as_view(), name='order'),
    url(r'^storage/$', views.StorageView.as_view(), name='storage'),
    url(r'^api/', include('control.api_urls', app_name='control', namespace='api'))
]