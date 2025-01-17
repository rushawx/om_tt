# Generated by Django 5.1.2 on 2024-10-21 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('h1', models.IntegerField(default=0)),
                ('h2', models.IntegerField(default=0)),
                ('h3', models.IntegerField(default=0)),
                ('a', models.JSONField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
