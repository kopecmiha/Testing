# Generated by Django 3.1.7 on 2022-06-14 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0007_auto_20220605_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testing',
            name='discipline',
        ),
    ]
