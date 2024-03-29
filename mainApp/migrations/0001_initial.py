# Generated by Django 3.1.6 on 2022-03-20 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logging',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now=True, db_column='Datetime')),
                ('lot', models.IntegerField(db_column='Lot')),
                ('status', models.IntegerField(db_column='Status')),
                ('weighing', models.FloatField(db_column='Weighing')),
            ],
            options={
                'db_table': 'Logging',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PrintHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=20)),
                ('imageurl', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=30, unique=True)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchno', models.CharField(max_length=10)),
                ('boxno', models.IntegerField()),
                ('status', models.IntegerField()),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
                ('weight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainApp.logging')),
            ],
        ),
        migrations.AddConstraint(
            model_name='register',
            constraint=models.UniqueConstraint(fields=('product', 'batchno', 'boxno'), name='productBatchnoBoxno'),
        ),
    ]
