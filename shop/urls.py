"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
from django.conf.urls import url, include

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings #new
from django.views.generic import TemplateView

import cart, clients, feedback, orders,products,suppliers
admin.autodiscover()

urlpatterns = [
    # path('admin/', admin.site.urls),

    url(r'^admin', include(admin.site.urls)),
    url(r'^products', include('products.urls', namespace='products')),
    url(r'^feedback', include('feedback.urls', namespace='feedback')),
    url(r'^info', TemplateView.as_view(template_name='info/info.html')),
    url(r'^shares', TemplateView.as_view(template_name='shares/shares.html')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^order/', include('orders.urls', namespace='orders')),

    url(r'^', TemplateView.as_view(template_name='index.html')),
]
