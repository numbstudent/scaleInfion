# Generated by Django 3.2.3 on 2022-08-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0046_weighingstate_expireddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weighingstate',
            name='expireddate',
            field=models.CharField(max_length=100),
        ),
    ]
