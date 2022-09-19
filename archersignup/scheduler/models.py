from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Offer(models.Model):
    Pick_Day = models.DateField(null=True)
# class pageInputs(models.Model):
#     name = models.CharField(max_length=300)
#     description = models.TextField(blank=True)
#     made_on = models.DateTimeField()