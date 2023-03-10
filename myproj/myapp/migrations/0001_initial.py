# Generated by Django 4.1.1 on 2022-10-29 05:01

import imp
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField(max_length=4)),
                ('course_name', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_id', models.IntegerField(max_length=7, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.EmailField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_num', models.IntegerField(max_length=30)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.IntegerField(max_length=30)),
                ('child', models.CharField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(max_length=30, unique=True)),
                ('course1', models.CharField(max_length=4)),
                ('course2', models.CharField(max_length=4)),
                ('course3', models.CharField(max_length=4)),
                ('course4', models.CharField(max_length=4)),
                ('course6', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(max_length=7, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('parent', models.CharField(max_length=100, unique=True)),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduated')], default='FR', max_length=2)),
            ],
        ),
    ]
