# Generated by Django 3.1.5 on 2021-01-17 04:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('image1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('blog_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('featured', models.BooleanField(default=False)),
                ('mvp', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category')),
            ],
        ),
    ]
