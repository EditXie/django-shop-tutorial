from django.conf.urls import url
from . import views

app_name = 'payment'

urlpatterns = [
    url(r'^process/$', views.payment_process),
    url(r'^done/$', views.payment_done),
    url(r'^canceled/$', views.payment_canceled),
]
