# Generated by Django 3.2.3 on 2022-08-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0034_weighingstate_weightadjustment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='jumlahkoli',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='weighingstate',
            name='jumlahkoli',
            field=models.IntegerField(default=0),
        ),
    ]