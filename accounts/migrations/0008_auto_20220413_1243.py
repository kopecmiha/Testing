# Generated by Django 3.1.7 on 2022-04-13 09:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220413_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=30, unique=True, verbose_name='Username'),
        ),
    ]