from django.conf import settings
from django.db import models
from django.utils import timezone

TIME_SLOTS = (
    ('9:30-9:40', '9:30-9:40'),
    ('9:40-9:50', '9:40-9:50'),
    ('9:50-10:00', '9:50-10:00'),
)


class signup(models.Model):
    Pick_Day = models.DateField(null=True)
    Pick_Time = models.CharField(max_length=10, choices=TIME_SLOTS, default='9:30-9:40')
    Name = models.CharField(max_length=15)
    
    # def __str__(self):
    #     return(self.Name, str(self.Pick_Day) + ': ' + str(self.Pick_Time))
    
