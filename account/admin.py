from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customuser
from .forms import CustomUserCreate , CustomUserUpdate
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreate
    form = CustomUserUpdate
    model = Customuser
    list_display = ['username','first_name','phone','password','role']
    fieldsets = (
        (None,{
            "fields":(
                'username','first_name',
                'phone','password','role'
            ),
        }),
    )

admin.site.register(Customuser,CustomUserAdmin)
