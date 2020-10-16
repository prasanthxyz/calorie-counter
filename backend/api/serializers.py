from rest_framework import serializers 
from api.models import FoodItem
 
 
class ApiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = FoodItem
        fields = ('id',
                  'userid',
                  'item',
                  'calorie')