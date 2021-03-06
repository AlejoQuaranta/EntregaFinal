# Generated by Django 4.0.4 on 2022-06-16 23:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=40)),
                ('cuerpo', models.CharField(max_length=1000)),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
        ),
    ]
