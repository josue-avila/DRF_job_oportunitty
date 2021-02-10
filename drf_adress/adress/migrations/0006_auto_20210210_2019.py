# Generated by Django 3.1.6 on 2021-02-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adress', '0005_auto_20210210_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adress',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adress',
            name='district',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adress',
            name='number',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='adress',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adress',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
