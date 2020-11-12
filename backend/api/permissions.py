""" Permissions for Calorie Counter """
from rest_framework import permissions
from api.models import FoodItem


class IsOwner(permissions.BasePermission):
    """ Permission to check ownership for DailyLog Access
        Authorized only if
        1. safe-method, or
        2. delete (permission handled in queryset), or
        3. if owner of the food item """

    message = 'Unauthorized.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS + ('DELETE',):
            return True

        fooditem_id = request.data.get('item')
        try:
            fooditem = FoodItem.objects.get(pk=fooditem_id)
        except FoodItem.DoesNotExist:
            return False

        return request.user == fooditem.user

    def has_object_permission(self, request, view, obj):
        return obj.item.user == request.user
