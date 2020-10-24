from rest_framework import serializers 
from api.models import FoodItem, DailyLog

class FooditemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'


class DailylogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'
