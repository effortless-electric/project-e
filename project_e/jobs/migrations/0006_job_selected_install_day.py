# Generated by Django 2.2.7 on 2020-01-27 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200126_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='selected_install_day',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Selected Time'),
        ),
    ]