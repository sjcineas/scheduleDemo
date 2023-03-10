# Generated by Django 4.1.1 on 2022-12-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_course_course_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(default=3335),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='instructor_id',
            field=models.IntegerField(default=4852183, unique=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_id',
            field=models.IntegerField(default=8146492, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=1659140, unique=True),
        ),
    ]
