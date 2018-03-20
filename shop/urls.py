from django.conf.urls import url

from . import views

app_name = 'shop' # django 1.9 后 取消include namespace

urlpatterns = [
    url(r'^$', views.product_list,name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list, name='product_list_by_category'),
    url(r'^(?P<product_id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail, name='product_detail')
    ]
