# Generated by Django 5.1.7 on 2025-03-31 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.CharField(max_length=50)),
                ('student_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=10)),
                ('new_course', models.CharField(max_length=10)),
            ],
        ),
    ]
