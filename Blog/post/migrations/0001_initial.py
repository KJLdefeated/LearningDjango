# Generated by Django 4.0.3 on 2022-03-16 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=10000000)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
