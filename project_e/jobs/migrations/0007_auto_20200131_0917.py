# Generated by Django 2.2.7 on 2020-01-31 14:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_job_selected_install_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='car_year',
            field=models.IntegerField(default=1999, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='contract_price',
            field=models.IntegerField(default=2500, max_length=6),
        ),
        migrations.AddField(
            model_name='job',
            name='customer_address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='car_make',
            field=models.CharField(default='Ford', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='car_model',
            field=models.CharField(default='Focus', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_to_job', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='dealership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dealers.Dealer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='sale_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date of Sale'),
        ),
        migrations.AlterField(
            model_name='job',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='seller_to_job', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='vin',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
    ]
