# Generated by Django 3.0.6 on 2020-05-31 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_auto_20200529_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default='会社名', max_length=100, verbose_name='企業名'),
        ),
    ]
