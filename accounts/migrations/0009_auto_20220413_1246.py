# Generated by Django 3.1.7 on 2022-04-13 09:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220413_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100, unique=True, verbose_name='Username'),
        ),
    ]
