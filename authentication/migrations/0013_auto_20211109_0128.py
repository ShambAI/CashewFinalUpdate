# Generated by Django 3.2.5 on 2021-11-09 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20211109_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communesatellite',
            name='country_comm',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='communesatellite',
            name='department_comm',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='deptsatellite',
            name='country_dept',
            field=models.CharField(max_length=200),
        ),
    ]
