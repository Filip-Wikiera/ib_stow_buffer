from .abstract import Area_Count
from django.db import models


class TSO(Area_Count):

    bufor_wozkow = models.PositiveIntegerField(default=0)
    name = "TSO"

    def total(self):
        return self.bufor_wozkow
