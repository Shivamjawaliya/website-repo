# Generated by Django 5.1.7 on 2025-04-01 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='course_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='decs',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='url',
            field=models.CharField(max_length=10000),
        ),
    ]
