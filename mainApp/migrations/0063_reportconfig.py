# Generated by Django 3.1.6 on 2024-01-24 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0062_auto_20221218_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchno', models.CharField(max_length=15)),
                ('pdf_form', models.CharField(default='FORM', max_length=50)),
                ('pdf_dn', models.CharField(default='DN', max_length=50)),
                ('pdf_dn_value', models.CharField(default='NOT ASSIGNED', max_length=20)),
                ('pdf_eff_date', models.CharField(default='Eff. Date', max_length=50)),
                ('pdf_eff_date_value', models.DateTimeField()),
                ('pdf_will_be_reviewed', models.CharField(default='This document will be reviewed on', max_length=50)),
                ('pdf_will_be_reviewed_value', models.DateTimeField()),
                ('pdf_rev_of_dn', models.CharField(default='Rev. of DN', max_length=50)),
                ('pdf_rev_of_dn_value', models.CharField(default='NOT ASSIGNED', max_length=20)),
                ('pdf_dn_date', models.CharField(default='Date', max_length=50)),
                ('pdf_nama_produk', models.CharField(default='Nama Produk', max_length=50)),
                ('pdf_no_batch', models.CharField(default='No Batch', max_length=50)),
                ('pdf_expired_date', models.CharField(default='Expired Date', max_length=50)),
                ('pdf_tanggal_penimbangan', models.CharField(default='Tanggal Penimbangan', max_length=50)),
                ('pdf_no_karton', models.CharField(default='No Karton', max_length=50)),
                ('pdf_hasil_penimbangan', models.CharField(default='Hasil Penimbangan', max_length=50)),
                ('pdf_dilakukan_oleh', models.CharField(default='Dilakukan oleh', max_length=50)),
                ('pdf_diperiksa_oleh', models.CharField(default='Diperiksa oleh', max_length=50)),
                ('pdf_diverifikasi_oleh', models.CharField(default='Diverifikasi oleh', max_length=50)),
                ('pdf_user_1', models.CharField(default='Petugas Penimbangan', max_length=50)),
                ('pdf_user_2', models.CharField(default='Petugas Gudang', max_length=50)),
                ('pdf_user_3', models.CharField(default='Supervisor Produksi', max_length=50)),
                ('pdf_user_4', models.CharField(default='Supervisor Gudang', max_length=50)),
                ('pdf_paraf', models.CharField(default='Paraf', max_length=50)),
                ('pdf_nama', models.CharField(default='Nama', max_length=50)),
                ('pdf_tanggal_paraf', models.CharField(default='Supervisor DS&S', max_length=50)),
                ('pdf_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='mainApp.department')),
                ('pdf_reporttitle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='mainApp.reporttitle')),
            ],
        ),
    ]
