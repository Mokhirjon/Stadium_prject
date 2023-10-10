from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customuser


# create new user
class CustomUserCreate(UserCreationForm):
    class Mete(UserCreationForm):
        model = Customuser
        fields = ('username', 'first_name',  'phone',  'password', 'role')


# update user

class CustomUserUpdate(UserChangeForm):
    class Meta(UserChangeForm):
        model = Customuser
        fields = ('username', 'first_name', 'phone', 'password', 'role')