# Generated by Django 3.2.3 on 2022-03-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_uploadedregister_measuredate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='batchno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='report',
            name='batchno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='uploadedregister',
            name='batchno',
            field=models.CharField(max_length=15),
        ),
    ]
