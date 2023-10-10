from django.contrib import admin

# Register your models here.
from .models import BronModel

class BronModelAdmin(admin.ModelAdmin):
    list_display = ('bron_name', 'begin_time', 'end_time', 'free_time', 'broned')
    search_fields = ['bron_name', 'broned']

admin.site.register(BronModel,BronModelAdmin)
