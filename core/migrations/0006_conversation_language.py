# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_conversation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='language',
            field=models.CharField(default='English', max_length=50),
        ),
    ]
