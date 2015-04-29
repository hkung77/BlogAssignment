from django.conf.urls import url 

from . import views

urlpatterns = [
        # Base url
        url(r'^$', views.index, name='index'),
        # This url handles all the individual  blog posts
        url(r'(?P<ID>[0-9]+)/$', views.detail, name='detail'),
]
