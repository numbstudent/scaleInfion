# Generated by Django 3.2.3 on 2022-08-15 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0045_alter_weighingstate_petugasgudang'),
    ]

    operations = [
        migrations.AddField(
            model_name='weighingstate',
            name='expireddate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
