# Generated by Django 3.1.7 on 2022-04-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_auto_20220414_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testing',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Title'),
        ),
    ]
