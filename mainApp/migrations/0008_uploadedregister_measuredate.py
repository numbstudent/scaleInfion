# Generated by Django 3.2.3 on 2022-03-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_uploadedregister_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedregister',
            name='measuredate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]