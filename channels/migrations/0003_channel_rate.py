# Generated by Django 4.0 on 2022-01-11 12:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='rate',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]