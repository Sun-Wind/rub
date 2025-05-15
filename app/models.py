from django.db import models

# Create your models here.
class Reviews(models.Model):
    num = models.SmallIntegerField()
    name = models.CharField(max_length=15)
    pro = models.FloatField
def __init__(self):
    return "%d:%s:%lf"%(self.num,self.name,self.pro)
class Meta:
        db_table="rub"
