# Generated by Django 3.2.1 on 2021-05-04 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="num_lections",
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
