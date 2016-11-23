from django.db import models
from django.utils import timezone
# Create your models here.

class Timer(models.Model):
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 50)
    buddy = models.EmailField()
    habit = models.TextField()
    created = models.DateTimeField(default = timezone.now)
    checkin_time = models.DurationField(default = timedelta(days = 1))
    checked_in = False

    def check_in():
        
