from django.contrib import admin

# Register your models here.
from .models import StadiumModel
from config.forms import Stadiumforms
class StadiumModelAdmin(admin.ModelAdmin):
    form = Stadiumforms
    list_display = ('stadium_name', 'stadium_address', 'contact', 'stadium_image', 'Bron_price', 'stadium_bio', 'stadium_rules', 'user')
    search_fields = ['stadium_name', 'stadium_address', 'contact']

admin.site.register(StadiumModel,StadiumModelAdmin)