# Generated by Django 3.2.1 on 2021-05-05 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_num_lections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='num_lections',
            field=models.PositiveIntegerField(),
        ),
    ]
