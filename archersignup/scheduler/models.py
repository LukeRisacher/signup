from django.conf import settings
from django.db import models
from django.utils import timezone

TIME_SLOTS = (
    ('9:30-9:40', '9:30-9:40'),
    ('9:40-9:50', '9:40-9:50'),
    ('9:50-9:55', '9:50-9:55'),
)


class Offer(models.Model):
    Pick_Day = models.DateField(null=True)
    Pick_Time = models.CharField(max_length=9, choices=TIME_SLOTS, default='9:30-9:40')
    
