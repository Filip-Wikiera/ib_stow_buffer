from django.forms import ModelForm
from .models.p1 import P1
from .models.p2 import P2
from .models.p3 import P3
from .models.p4 import P4
from .model.trans import Trans
from .model.tso import TSO


class P1Form(ModelForm):
    class Meta:
        model = P1
        fields = ["user","AP_JUICE","AP_UBOT","BUTY_JUICE",
        "BUTY_UBOT", "HL_JUICE", "HL_UBOT",
		"NS_JUICE", "NS_UBOT", "TRANS", "DAMAGE", "KONSOLA", "PS_CRET", "HANGERS"]


class P2Form(ModelForm):
    class Meta:
        model = P2
        fields = ["user","AP_JUICE","AP_UBOT","BUTY_JUICE",
        "BUTY_UBOT", "HL_JUICE", "HL_UBOT",
		"NS_JUICE", "NS_UBOT", "TRANS", "DAMAGE", "KONSOLA", "PS_CRET", "HANGERS"]


class P3Form(ModelForm):
    class Meta:
        model = P3
        fields = ["user","AP_JUICE","AP_UBOT","BUTY_JUICE",
        "BUTY_UBOT", "HL_JUICE", "HL_UBOT",
		"NS_JUICE", "NS_UBOT", "TRANS", "DAMAGE", "KONSOLA", "PS_CRET", "HANGERS"]


class P4Form(ModelForm):
    class Meta:
        model = P4
        fields = ["user","AP_JUICE","AP_UBOT","BUTY_JUICE",
        "BUTY_UBOT", "HL_JUICE", "HL_UBOT",
		"NS_JUICE", "NS_UBOT", "TRANS", "DAMAGE", "KONSOLA", "PS_CRET", "HANGERS"]



class TransForm(ModelForm):
    class Meta:
        model = Trans
        fields = ["user","TRANS","TRANS_DMG","NYR","ZBUDOWANE","SHIFTPLAN"]


class TSOForm(ModelForm):
    class Meta:
        model = TSO
        fields = ["user","bufor_wozkow"]