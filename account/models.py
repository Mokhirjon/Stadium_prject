from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.


class Customuser(AbstractUser):
    CHOICE_ROLES = (
        (3,'admin'),
        (2,'owner'),
        (1, 'broner')
    )

    role = models.PositiveSmallIntegerField(default=1,choices=CHOICE_ROLES)
    phone = models.CharField(default='',max_length=15)