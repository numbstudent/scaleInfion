from email.policy import default
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30, unique=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

class Logging(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', auto_now=True)  # Field name made lowercase.
    lot = models.IntegerField(db_column='Lot')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    weighing = models.FloatField(db_column='Weighing')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Logging'

class Register(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    batchno = models.CharField(max_length=10)
    boxno = models.IntegerField()
    status = models.IntegerField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    weight = models.ForeignKey(Logging, null=True, on_delete=models.DO_NOTHING)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'batchno', 'boxno'], name='productBatchnoBoxno')
        ]

class PrintHeader(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=20)
    imageurl = models.CharField(max_length=100)