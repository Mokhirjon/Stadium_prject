from django.db import models
from datetime import datetime
# Create your models here.


class BronModel(models.Model):
    bron_name = models.CharField(max_length=120,default='')
    begin_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    free_time = models.DateTimeField(default=datetime.now)
    broned = models.BooleanField(default=False)



    def __str__(self) -> str:
        return self.bron_name

    class Meta:
        db_table = 'Bron'    
