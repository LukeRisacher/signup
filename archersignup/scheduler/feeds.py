from django.contrib.syndication.views import Feed
from django.urls import reverse
import datetime as dt
from .models import signup

class AllSignUps(Feed):
    title = 'Signup site'
    link = '/all_signups'
    description = 'Updates on signups'
    
    def items(self):
        return signup.objects.all()
    
    def item_title(self, item):
        return item.Name
    
    def item_description(self, item):
        return item.Pick_Time, item.Pick_Day.strftime('%m-%d-%Y')
    
    def item_name(self, item):
        return item.Name