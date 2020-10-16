# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.models import FoodItem
from api.serializers import ApiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def fooditem_list(request):
    if request.method == 'GET':
        fooditems = FoodItem.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            fooditems = fooditems.filter(title__icontains=title)
        
        api_serializer = ApiSerializer(fooditems, many=True)
        return JsonResponse(api_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        fooditem_data = JSONParser().parse(request)
        fooditem_serializer = ApiSerializer(data=fooditem_data)
        if fooditem_serializer.is_valid():
            fooditem_serializer.save()
            return JsonResponse(fooditem_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(fooditem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = FoodItem.objects.all().delete()
        return JsonResponse({'message': '{} FoodItems were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def fooditem_detail(request, pk):
    try: 
        fooditem = FoodItem.objects.get(pk=pk) 
    except FoodItem.DoesNotExist: 
        return JsonResponse({'message': 'The fooditem does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        fooditem_serializer = ApiSerializer(fooditem) 
        return JsonResponse(fooditem_serializer.data) 
 
    elif request.method == 'PUT': 
        fooditem_data = JSONParser().parse(request) 
        fooditem_serializer = ApiSerializer(fooditem, data=fooditem_data) 
        if fooditem_serializer.is_valid(): 
            fooditem_serializer.save() 
            return JsonResponse(fooditem_serializer.data) 
        return JsonResponse(fooditem_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        fooditem.delete() 
        return JsonResponse({'message': 'FoodItem was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
