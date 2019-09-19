from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/bus$', views.bus, name='bus'),
    url(r'^search/bus_result$', views.bus_result, name='bus_result'),
    url(r'^search/tur$', views.tur, name='tur'),
    url(r'^search/help', views.help, name='tur'),
    url(r'^search/plane$', views.plane, name='plane'),
    url(r'^search/vizas$', views.vizas, name='vizas'),
    url(r'^search/hot$', views.hot, name='hot'),
    url(r'^search/days$', views.days, name='days'),
    url(r'^search/podbor-tura/$', views.podbor_tura, name='podbor_tura'),
    url(r'^podbor-tura/$', views.podbor_tura, name='podbor_tura'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^about/$', views.about, name="about"),

    url(r'^order/order$', views.order, name='order'),
    url(r'^order/sms_order$', views.sms_order, name='sms_order')

    ]