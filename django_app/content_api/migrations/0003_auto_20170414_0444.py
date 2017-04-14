# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 04:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content_api', '0002_auto_20170413_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_api.Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='bookmarks',
            field=models.ManyToManyField(null=True, through='content_api.Bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]
