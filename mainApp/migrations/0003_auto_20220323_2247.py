# Generated by Django 3.1.6 on 2022-03-23 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='batchno',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainApp.product'),
        ),
    ]
