from django.conf.urls import url
from . import views_user, views_food

urlpatterns = [
    url(r'^signup$', views_user.signup, name='signup'),
    url(r'^login$', views_user.login, name='login'),
    url(r'^logout$', views_user.logout, name='logout'),
    url(r'^closeaccount$', views_user.closeaccount, name='closeaccount'),
    url(r'^fooditem$', views_food.fooditem, name='fooditem'),
]
