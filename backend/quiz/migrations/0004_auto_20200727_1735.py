# Generated by Django 2.2.10 on 2020-07-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20200727_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
