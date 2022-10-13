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
    jumlahkoli = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True,choices=STATUS_CHOICES)
    createdby = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="createdby")
    updatedby = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name="updatedby")
    def __str__(self):
        return self.name


class ProductHistory(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    minweight = models.FloatField()
    maxweight = models.FloatField()
    standardweight = models.FloatField()
    jumlahkoli = models.IntegerField(default=0)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True, choices=STATUS_CHOICES)
    createdby = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="createdbyhistory")
    updatedby = models.ForeignKey(
        User, on_delete=models.RESTRICT, null=True, blank=True, related_name="updatedbyhistory")

    def __str__(self):
        return self.name


class ProductUploadTemp(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    minweight = models.FloatField()
    maxweight = models.FloatField()
    standardweight = models.FloatField()
    jumlahkoli = models.IntegerField(default=0)
    createdby = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="createdbytemp")
    createdon = models.DateTimeField(auto_now_add=True, blank=True)
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
    # operator1 = models.CharField(max_length=50, default=None, null=True)
    # operator2 = models.CharField(max_length=50, default=None, null=True)
    operator = models.CharField(max_length=50, default=None, null=True)
    petugasgudang = models.CharField(max_length=50, default=None, null=True)
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
    signingdate = models.DateTimeField(blank=True, null=True)
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
    weightadjustment = models.FloatField(default=0)
    jumlahkoli = models.IntegerField(default=0)
    spvpabrik = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="spvpabrik", null=True) #boleh kosong di create awal batchno
    spvgudang = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="spvgudang", null=True) #boleh kosong di create awal batchno
    operator = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="operator", null=True) #boleh kosong di create awal batchno
    petugasgudang = models.CharField(max_length=50, default=None, null=True)
    expireddate = models.CharField(max_length=20)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

class ReportRegister(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    dnrev = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    batchno = models.CharField(max_length=15)
    boxno = models.IntegerField()
    status = models.IntegerField(null=True, default=None)
    # operator1 = models.CharField(max_length=50, default=None, null=True)
    # operator2 = models.CharField(max_length=50, default=None, null=True)
    operator = models.CharField(max_length=50, default=None, null=True)
    petugasgudang = models.CharField(max_length=50, default=None, null=True)
    createdon = models.DateTimeField(null=True)
    weight = models.FloatField(null=True)
    createdby = models.ForeignKey(User, on_delete=models.RESTRICT)


class AdminConfig(models.Model):
    spvapproval = models.BooleanField(default=False)
    spvapprovalexpireddate = models.DateTimeField(blank=True, null=True, default=None)
    operator = models.CharField(max_length=50, default=None, null=True)
    petugasgudang = models.CharField(max_length=50, default=None, null=True)
    weightadjustment = models.FloatField(default=0)

    # report pdf
    pdf_form = models.CharField(max_length=50, default="FORM", null=False)
    pdf_dn = models.CharField(max_length=50, default="DN", null=False)
    pdf_dn_value = models.CharField(max_length=20, default="NOT ASSIGNED")
    pdf_eff_date = models.CharField(max_length=50, default="Eff. Date", null=False)
    pdf_eff_date_value = models.DateTimeField(null=False)
    pdf_will_be_reviewed = models.CharField(max_length=50, default="This document will be reviewed on", null=False)
    pdf_will_be_reviewed_value = models.DateTimeField(null=False)
    pdf_rev_of_dn = models.CharField(max_length=50, default="Rev. of DN", null=False)
    pdf_dn_date = models.CharField(max_length=50, default="Date", null=False)
    pdf_reporttitle = models.ForeignKey(ReportTitle, on_delete=models.RESTRICT, null=True)
    pdf_department = models.ForeignKey(Department, on_delete=models.RESTRICT, null=True)
    pdf_nama_produk = models.CharField(max_length=50, default="Nama Produk", null=False)
    pdf_no_batch = models.CharField(max_length=50, default="No Batch", null=False)
    pdf_expired_date = models.CharField(max_length=50, default="Expired Date", null=False)
    pdf_tanggal_penimbangan = models.CharField(max_length=50, default="Tanggal Penimbangan", null=False)
    pdf_no_karton = models.CharField(max_length=50, default="No Karton", null=False)
    pdf_hasil_penimbangan = models.CharField(
        max_length=50, default="Hasil Penimbangan", null=False)
    pdf_dilakukan_oleh = models.CharField(max_length=50, default="Dilakukan oleh", null=False)
    pdf_diperiksa_oleh = models.CharField(max_length=50, default="Diperiksa oleh", null=False)
    pdf_diverifikasi_oleh = models.CharField(
        max_length=50, default="Diverifikasi oleh", null=False)
    pdf_user_1 = models.CharField(
        max_length=50, default="Petugas Penimbangan", null=False)
    pdf_user_2 = models.CharField(
        max_length=50, default="Petugas Gudang", null=False)
    pdf_user_3 = models.CharField(
        max_length=50, default="Supervisor Produksi", null=False)
    pdf_user_4 = models.CharField(max_length=50, default="Supervisor Gudang", null=False)
    pdf_paraf = models.CharField(max_length=50, default="Paraf", null=False)
    pdf_nama = models.CharField(max_length=50, default="Nama", null=False)
    pdf_tanggal_paraf = models.CharField(
        max_length=50, default="Supervisor DS&S", null=False)

class ReprintList(models.Model):
    register = models.ForeignKey(Register, on_delete=models.RESTRICT)
    createdon = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)