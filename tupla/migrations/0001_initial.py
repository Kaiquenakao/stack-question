# Generated by Django 3.2.9 on 2022-11-02 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('github', models.CharField(max_length=500)),
                ('technology', models.IntegerField(choices=[(0, 'JavaScript'), (1, 'Java'), (2, 'Python'), (4, 'Android'), (5, 'Apple'), (6, 'Other')], default=6)),
                ('summary', models.TextField(max_length=200)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 11, 2, 9, 34, 59, 812819))),
                ('project_image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'ordering': ['technology'],
            },
        ),
    ]