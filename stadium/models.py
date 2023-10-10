from django.db import models
from account.models import Customuser
# Create your models here.


class StadiumModel(models.Model):
    stadium_name = models.CharField(max_length=150,default='')
    stadium_address = models.URLField()
    contact = models.CharField(max_length=20,default='')
    stadium_image = models.ImageField(upload_to='Stadium/')
    Bron_price = models.FloatField(default=0)
    stadium_bio = models.TextField(default='')
    stadium_rules = models.TextField(default='')
    user = models.ForeignKey(Customuser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.stadium_name

    class Meta:
        db_table = 'Stadium'
