# Generated by Django 3.1.6 on 2022-06-09 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0025_auto_20220609_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='product',
            field=models.ForeignKey(default=38, on_delete=django.db.models.deletion.RESTRICT, to='mainApp.product'),
            preserve_default=False,
        ),
    ]
