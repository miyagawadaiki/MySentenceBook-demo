# Generated by Django 2.2.2 on 2019-06-30 02:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sentences', '0002_auto_20190630_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date updated'),
        ),
    ]
