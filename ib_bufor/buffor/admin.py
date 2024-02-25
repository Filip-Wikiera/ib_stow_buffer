from django.contrib import admin
from .models.p1 import P1
from .models.p2 import P2
from .models.p3 import P3
from .models.p4 import P4
from .models.tso import TSO
from .models.trans import Trans

# Register your models here.


class FloorAdmin(admin.ModelAdmin):
    pass


class Area_CountAdmin(admin.ModelAdmin):
    pass


admin.site.register(P1, FloorAdmin)
admin.site.register(P2, FloorAdmin)
admin.site.register(P3, FloorAdmin)
admin.site.register(P4, FloorAdmin)
admin.site.register(TSO, Area_CountAdmin)
admin.site.register(Trans, Area_CountAdmin)



