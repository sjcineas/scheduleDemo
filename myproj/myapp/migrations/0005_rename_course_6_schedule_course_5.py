# Generated by Django 4.1.1 on 2022-10-29 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_course1_schedule_course_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='course_6',
            new_name='course_5',
        ),
    ]
