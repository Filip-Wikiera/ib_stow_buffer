from django.db import models
import datetime
# Create your models here.


class Area_Count(models.Model):
    user = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(auto_now_add=True)
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
