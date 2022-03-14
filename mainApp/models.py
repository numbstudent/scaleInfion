from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30, unique=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)


class Register(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batchno = models.CharField(max_length=10)
    boxno = models.IntegerField()
    status = models.IntegerField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'batchno', 'boxno'], name='productBatchnoBoxno')
        ]


class Logging(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    weighing = models.FloatField()
    register = models.ForeignKey(
        Register, on_delete=models.CASCADE, blank=True, null=True)


class PrintHeader(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=20)
    imageurl = models.CharField(max_length=100)
