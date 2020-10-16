from django.db import models

# Create your models here.
class FoodItem(models.Model):
    userid = models.IntegerField(blank=False, default=1)
    item = models.CharField(max_length=70, blank=False, default='')
    calorie = models.DecimalField(max_digits=5, decimal_places=2, blank=False, default=0.00)

