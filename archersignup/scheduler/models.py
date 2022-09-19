from django.conf import settings
from django.db import models
from django.utils import timezone


class Offer(models.Model):
    Pick_Day = models.DateField(null=True)
