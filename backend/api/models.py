from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

# Create your models here.
class FoodItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    item = models.CharField(max_length=200, blank=False, null=False)
    calorie = models.DecimalField(max_digits=7, decimal_places=5, default=0)


class DailyLog(models.Model):
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    day = models.DateField(default=date.today)
    quantity = models.IntegerField(default=0)
