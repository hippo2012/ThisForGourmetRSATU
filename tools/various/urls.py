from django.conf.urls import patterns, url

urlpatterns = patterns('tools.various.views',
                       url(r'^logout/$', 'user_logout', name='control-logout'), )

