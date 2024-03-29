# Generated by Django 3.2.3 on 2022-04-15 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20220406_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='standardweight',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProductState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mainApp.product')),
            ],
        ),
    ]
