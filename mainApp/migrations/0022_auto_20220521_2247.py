# Generated by Django 3.1.6 on 2022-05-21 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0021_auto_20220518_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weighingstate',
            name='batchno',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]