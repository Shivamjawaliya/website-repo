# Generated by Django 5.1.7 on 2025-04-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coourses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coourses',
            name='course_name',
            field=models.CharField(max_length=50),
        ),
    ]
