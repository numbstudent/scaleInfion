# Generated by Django 3.2.3 on 2022-09-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0054_auto_20220926_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminconfig',
            name='pdf_dn_value',
            field=models.CharField(default='NOT ASSIGNED', max_length=20),
        ),
        migrations.AlterField(
            model_name='adminconfig',
            name='pdf_eff_date_value',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='adminconfig',
            name='pdf_will_be_reviewed_value',
            field=models.DateTimeField(),
        ),
    ]
