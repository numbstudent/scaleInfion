# Generated by Django 3.2.3 on 2022-05-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0018_auto_20220420_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='weighingstate',
            name='pendingstatus',
            field=models.BooleanField(choices=[(True, 'Pending'), (False, 'Not Pending')], default=True),
        ),
    ]
