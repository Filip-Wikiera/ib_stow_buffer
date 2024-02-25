from .abstract import Floor
from django.db import models


class P1(Floor):

    AP_JUICE = models.PositiveIntegerField(default=0)
    AP_UBOT = models.PositiveIntegerField(default=0)
    BUTY_JUICE = models.PositiveIntegerField(default=0)
    BUTY_UBOT = models.PositiveIntegerField(default=0)
    HL_JUICE = models.PositiveIntegerField(default=0)
    HL_UBOT = models.PositiveIntegerField(default=0)
    NS_JUICE = models.PositiveIntegerField(default=0)
    NS_UBOT = models.PositiveIntegerField(default=0)
    TRANS = models.PositiveIntegerField(default=0)
    DAMAGE = models.PositiveIntegerField(default=0)
    KONSOLA = models.PositiveIntegerField(default=0)
    PS_CRET = models.PositiveIntegerField(default=0)
    HANGERS = models.PositiveIntegerField(default=0)

    name = "P1"

    def trans(self):
        return self.TRANS

    def app_total(self):
        return self.AP_UBOT+self.AP_JUICE

    def buty_total(self):
        return self.BUTY_JUICE+self.BUTY_UBOT

    def hl_total(self):
        return self.HL_JUICE+self.HL_UBOT

    def ns_total(self):
        return self.NS_JUICE+self.NS_UBOT

    def total(self):
        return self.AP_JUICE + self.AP_UBOT + self.BUTY_JUICE + self.BUTY_UBOT + self.HL_JUICE + self.HL_UBOT + self.NS_JUICE + self.NS_UBOT + self.TRANS + self.DAMAGE + self.KONSOLA + self.PS_CRET + self.HANGERS
