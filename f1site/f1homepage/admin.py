from django.contrib import admin
from .models import Qualifying
from .models import Driver
from .models import Final
from .models import Point

admin.site.register(Driver)
admin.site.register(Qualifying)
admin.site.register(Final)
admin.site.register(Point)



# Register your models here.
