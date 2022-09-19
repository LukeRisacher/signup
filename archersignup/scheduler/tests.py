from django.test import TestCase

# Create your tests here.
from django.db import models
 
class Offer(models.Model):
    expiration_date = models.DateField(null=True)