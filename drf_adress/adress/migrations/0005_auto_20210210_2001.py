# Generated by Django 3.1.6 on 2021-02-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adress', '0004_auto_20210210_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adress',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adress',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adress',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
