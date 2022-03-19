# Generated by Django 3.2.3 on 2022-03-17 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iot',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(db_column='Datetime')),
                ('lot', models.IntegerField(db_column='Lot')),
                ('status', models.IntegerField(db_column='Status')),
                ('weighing', models.FloatField(db_column='Weighing')),
            ],
            options={
                'db_table': 'IOT',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='register',
            name='weight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainApp.iot'),
        ),
    ]
