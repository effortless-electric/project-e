# Generated by Django 2.2.7 on 2020-01-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='Address')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
        ),
    ]
