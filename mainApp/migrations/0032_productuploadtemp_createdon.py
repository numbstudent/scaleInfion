# Generated by Django 3.1.6 on 2022-07-16 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0031_remove_productuploadtemp_updatedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='productuploadtemp',
            name='createdon',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]