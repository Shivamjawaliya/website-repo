# Generated by Django 5.1.7 on 2025-03-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='requestcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=10)),
                ('student_email', models.CharField(max_length=20)),
                ('course_teacher', models.CharField(max_length=30)),
            ],
        ),
    ]
