# Generated by Django 3.1.6 on 2022-07-16 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0030_productuploadtemp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productuploadtemp',
            name='updatedby',
        ),
    ]