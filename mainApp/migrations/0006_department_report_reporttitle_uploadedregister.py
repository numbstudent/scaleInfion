# Generated by Django 3.2.3 on 2022-03-28 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_product_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReportTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchno', models.CharField(max_length=10)),
                ('boxno', models.IntegerField()),
                ('weight', models.FloatField()),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchno', models.CharField(max_length=10)),
                ('reviewdate', models.DateTimeField(blank=True, null=True)),
                ('effectivedate', models.DateTimeField(blank=True, null=True)),
                ('dnno', models.CharField(blank=True, max_length=20, null=True)),
                ('dnrev', models.IntegerField()),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainApp.department')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainApp.product')),
                ('reporttitle', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainApp.reporttitle')),
            ],
        ),
    ]
