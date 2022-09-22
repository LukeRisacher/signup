from django.conf import settings
from django.db import models
from django.utils import timezone

TIME_SLOTS = (
    ('7:30-8:00', '7:30-8:00 (Before School)'),
    ('9:30-10:00', '9:30-10:00 (Archers)'),
)


class signup(models.Model):
    Pick_Day = models.DateField(null=True)
    Pick_Time = models.CharField(max_length=25, choices=TIME_SLOTS, default='9:30-10:00')
    Name = models.CharField(max_length=15)
    
    # def __str__(self):
    #     return(self.Name, str(self.Pick_Day) + ': ' + str(self.Pick_Time))
    
