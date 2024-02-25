from .abstract import Area_Count
from django.db import models


class Trans(Area_Count):
    TRANS = models.PositiveIntegerField(default=0)
    TRANS_DMG = models.PositiveIntegerField(default=0)
    NYR = models.PositiveIntegerField(default=0)
    ZBUDOWANE = models.PositiveIntegerField(default=0)
    SHIFTPLAN = models.PositiveIntegerField(default=0)

    name = "Trans"

    def total(self):
        return self.TRANS+self.TRANS_DMG
