# Generated by Django 3.1.7 on 2022-06-05 13:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0006_question_testing_array'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='testing',
        ),
        migrations.AlterField(
            model_name='question',
            name='testing_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), default=list, size=None, verbose_name='Test'),
        ),
    ]
