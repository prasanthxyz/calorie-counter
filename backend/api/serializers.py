"""
Serializers for calorie-counter
"""
from rest_framework import serializers
from api.models import FoodItem, DailyLog

class FoodItemSerializer(serializers.ModelSerializer):
    """ FoodItem Serializer """
    class Meta:
        model = FoodItem
        fields = '__all__'


class DailyLogSerializer(serializers.ModelSerializer):
    """ DailyLog Serializer """
    class Meta:
        model = DailyLog
        fields = '__all__'
