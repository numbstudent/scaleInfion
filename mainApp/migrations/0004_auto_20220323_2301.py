# Generated by Django 3.1.6 on 2022-03-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20220323_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='batchno',
            field=models.CharField(max_length=10),
        ),
    ]