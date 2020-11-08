from decimal import InvalidOperation
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api.models import FoodItem
from api.serializers import FooditemSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def fooditem(request):
    """
    Create, Retrieve, Update or Delete a FoodItem.
    """
    if request.method == 'GET':
        item = request.query_params.get('item')
        if item:
            try:
                food_item = FoodItem.objects.get(user=request.user, item=item)
                food_serializer = FooditemSerializer(food_item)
                return Response(food_serializer.data, status=status.HTTP_200_OK)
            except FoodItem.DoesNotExist:
                # The specified food item wasn't found, returning all food items instead
                pass

        fooditems = FoodItem.objects.all().filter(user=request.user)
        food_serializer = FooditemSerializer(fooditems, many=True)
        return Response(food_serializer.data, status=status.HTTP_200_OK)

    food_info = JSONParser().parse(request)

    if request.method == 'POST':
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
        return Response({"detail": "Path not implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)

    if 'item' not in food_info:
        return Response({"detail": "item not provided"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        food_item = FoodItem.objects.get(user=request.user, item=food_info['item'])
    except FoodItem.DoesNotExist:
        return Response({"detail": "Food item not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if 'calorie' not in food_info:
            return Response({"detail": "calorie not provided"}, status=status.HTTP_400_BAD_REQUEST)
        food_item.calorie = food_info['calorie']
        food_item.save()
        food_serializer = FooditemSerializer(food_item)
        return Response(food_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        food_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
