# Generated by Django 3.0.6 on 2020-05-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20200527_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='next_datetime',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
