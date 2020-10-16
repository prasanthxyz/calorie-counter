from django.conf.urls import url 
from api import views 
 
urlpatterns = [ 
    url(r'^api/fooditems$', views.fooditem_list),
    url(r'^api/fooditems/(?P<pk>[0-9]+)$', views.fooditem_detail)
]