# Generated by Django 4.0.1 on 2022-01-16 05:50

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
