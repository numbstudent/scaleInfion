from email.policy import default
from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = ((True, 'Aktif'), (False, 'Tidak Aktif'))
PENDING_CHOICES = ((1, 'Pending'), (0, 'Close'))

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30, unique=True)
    minweight = models.FloatField()
    maxweight = models.FloatField()
    standardweight = models.FloatField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True,choices=STATUS_CHOICES)
    createdby = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="createdby")
    updatedby = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name="updatedby")
    def __str__(self):
        return self.name

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
    batchno = models.CharField(max_length=15)
    boxno = models.IntegerField()
    status = models.IntegerField(null=True, default=None)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    weight = models.FloatField(null=True)
    createdby = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="createdby_rel")
    updatedby = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name="updatedby_rel")
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['product', 'batchno', 'boxno'], name='productBatchnoBoxno')
    #     ]

class PrintHeader(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=20)
    imageurl = models.CharField(max_length=100)



#REPORT MODELS
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ReportTitle(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Report(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    batchno = models.CharField(max_length=15)
    reporttitle = models.ForeignKey(ReportTitle, on_delete=models.RESTRICT)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    reviewdate = models.DateTimeField(blank=True, null=True)
    effectivedate = models.DateTimeField(blank=True, null=True)
    dnno = models.CharField(max_length=20,blank=True, null=True)
    dnrev = models.IntegerField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)


class UploadedRegister(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    batchno = models.CharField(max_length=15)
    boxno = models.IntegerField()
    weight = models.FloatField()
    measuredate = models.DateTimeField(null=True, blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

class WeighingState(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    batchno = models.CharField(max_length=15, unique=True)
    status = models.BooleanField(default=True,choices=STATUS_CHOICES)
    pendingstatus = models.BooleanField(default=True,choices=PENDING_CHOICES) #pendingstatus true = masih belum close
    spvpabrik = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="spvpabrik", null=True) #boleh kosong di create awal batchno
    spvgudang = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="spvgudang", null=True) #boleh kosong di create awal batchno
    operator = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="operator", null=True) #boleh kosong di create awal batchno
    petugasgudang = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="petugasgudang", null=True) #boleh kosong di create awal batchno
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

class ReportRegister(models.Model):
    dnrev = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    batchno = models.CharField(max_length=15)
    boxno = models.IntegerField()
    status = models.IntegerField(null=True, default=None)
    createdon = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField(null=True)
    createdby = models.ForeignKey(User, on_delete=models.RESTRICT)