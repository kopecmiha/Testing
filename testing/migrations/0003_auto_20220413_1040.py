# Generated by Django 3.1.7 on 2022-04-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20220412_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Question'),
        ),
    ]
