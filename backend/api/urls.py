"""
Urls for calorie-counter
"""
from django.conf.urls import url, include
from rest_framework import routers
from . import views_user, views_food

router = routers.DefaultRouter()
router.register(r'fooditems', views_food.FoodItemViewSet, basename='fooditems')

urlpatterns = [
    url(r'^signup$', views_user.signup, name='signup'),
    url(r'^login$', views_user.login, name='login'),
    url(r'^logout$', views_user.logout, name='logout'),
    url(r'^closeaccount$', views_user.closeaccount, name='closeaccount'),
    url(r'^v1/', include(router.urls)),
]
