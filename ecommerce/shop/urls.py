from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url('', views.product_list, name='product_list'),
    url('^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url('^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
