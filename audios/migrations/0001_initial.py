# Generated by Django 4.0 on 2022-01-14 07:46

import audios.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('path', models.FileField(upload_to=audios.models.upload_to)),
                ('poster', models.ImageField(default='media\\default-user.png', upload_to=audios.models.upload_to)),
            ],
        ),
    ]
