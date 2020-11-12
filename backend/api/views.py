""" Views for FoodItem and DailyLog """
from rest_framework import viewsets
from api.models import FoodItem, DailyLog
from api.serializers import FoodItemSerializer, DailyLogSerializer
from api.permissions import IsOwner


class FoodItemViewSet(viewsets.ModelViewSet):
    """ FoodItem CRUD ViewSet """
    serializer_class = FoodItemSerializer

    def get_queryset(self):
        return FoodItem.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data.update({'user': request.user.id})
        return super(FoodItemViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        request.data.update({'user': request.user.id})
        # pylint: disable=no-member
        return super(FoodItemViewSet, self).partial_update(request, *args, **kwargs)


class DailyLogViewSet(viewsets.ModelViewSet):
    """ DailyLog CRUD ViewSet """
    serializer_class = DailyLogSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return DailyLog.objects.filter(item__user=self.request.user)
