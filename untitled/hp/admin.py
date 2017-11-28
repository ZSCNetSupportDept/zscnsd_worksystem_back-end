from django.contrib import admin

# Register your models here.
from .models import HP, DeBuff, Buff

admin.site.register(HP)
admin.site.register(DeBuff)
admin.site.register(Buff)
