""" Models for calorie-counter """
from datetime import date
from django.db import models
from django.contrib.auth import get_user_model

class FoodItem(models.Model):
    """ FoodItem model """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    calorie = models.DecimalField(max_digits=7, decimal_places=5, default=0)

    class Meta:
        unique_together = ('user', 'name',)

    def __str__(self):
        # pylint: disable=no-member
        return '{} ({}): {} cals'.format(self.name, self.user.username, self.calorie)

class DailyLog(models.Model):
    """ DailyLog model """
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    day = models.DateField(default=date.today)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}: {} {}'.format(self.day, self.item.user.username, self.quantity, self.item.name)
