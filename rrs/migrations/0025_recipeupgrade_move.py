# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-18 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0024_recipeupgrade_downgrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeupgrade',
            name='orig_filepath',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='recipeupgrade',
            name='upgrade_type',
            field=models.CharField(choices=[('U', 'Upgrade'), ('D', 'Downgrade'), ('N', 'Delete'), ('R', 'Delete (final)'), ('M', 'Move')], db_index=True, default='U', max_length=1),
        ),
    ]
