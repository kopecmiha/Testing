# Generated by Django 3.1.7 on 2022-04-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='title',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='Title'),
        ),
    ]
