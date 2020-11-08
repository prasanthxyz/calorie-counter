from decimal import InvalidOperation
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
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
    elif request.method == 'POST':
        food_info = JSONParser().parse(request)
        if 'item' not in food_info or 'calorie' not in food_info:
            return Response({"detail": "item or calorie not provided"}, status=status.HTTP_400_BAD_REQUEST)

        item, calorie = food_info['item'], food_info['calorie']
        try:
            FoodItem.objects.get(user=request.user, item=item)
            return Response({"detail": "food item already exists, please modify the existing item"}, status=status.HTTP_400_BAD_REQUEST)
        except FoodItem.DoesNotExist:
            pass

        try:
            food_item = FoodItem.objects.create(user=request.user, item=item, calorie=calorie)
            food_serializer = FooditemSerializer(food_item)
            return Response(food_serializer.data, status=status.HTTP_201_CREATED)
        except InvalidOperation:
            return Response({"detail": "Please recheck the values (the calorie should have max 2 digits and max 5 decimal points)"}, status=status.HTTP_400_BAD_REQUEST)
