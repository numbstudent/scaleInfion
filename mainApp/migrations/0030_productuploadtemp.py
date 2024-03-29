# Generated by Django 3.1.6 on 2022-07-16 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0029_producthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductUploadTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=30)),
                ('minweight', models.FloatField()),
                ('maxweight', models.FloatField()),
                ('standardweight', models.FloatField()),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='createdbytemp', to=settings.AUTH_USER_MODEL)),
                ('updatedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='updatedbytemp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
