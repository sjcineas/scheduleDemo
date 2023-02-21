# Generated by Django 4.1.1 on 2022-11-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_course_course_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(default=6925),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='instructor_id',
            field=models.IntegerField(default=3942696, unique=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parent_id',
            field=models.IntegerField(default=4559361, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=2446154, unique=True),
        ),
    ]