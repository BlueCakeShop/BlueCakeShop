from django.conf.urls import url
from django.core.urlresolvers import reverse
#from django.contrib import admin
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^$', views.product_list, name='product_list'),
]
