from django.db import models
import datetime
from datetime import timedelta
from django.utils import timezone

def one_hour_from_now():
    return timezone.now() + timedelta(hours=1)
# Create your models here.


class Area_Count(models.Model):
    user = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(default=one_hour_from_now)
    name = ""

    class Meta:
        abstract = True

    def total(self):
        pass

    def __str__(self):
        date = self.time_stamp.strftime("%d/%m/%Y %H:%M")
        return f"{self.name} {date} Total: {self.total()}"


class Floor(Area_Count):

    class Meta:
        abstract = True

    def trans(self):
        pass
