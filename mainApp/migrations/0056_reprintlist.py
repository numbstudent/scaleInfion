# Generated by Django 3.2.3 on 2022-10-11 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0055_auto_20220927_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReprintList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('register', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainApp.register')),
            ],
        ),
    ]