from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import FoodItem
from api.serializers import FooditemSerializer


@api_view(['GET', 'POST', 'DELETE'])
def fooditem(request):
    if request.method == 'GET':
        fooditems = FoodItem.objects.all().filter(user=request.user)
        food_serializer = FooditemSerializer(fooditems, many=True)
        return Response(food_serializer.data, status=status.HTTP_200_OK)
