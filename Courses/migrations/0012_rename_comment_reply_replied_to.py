# Generated by Django 4.0.1 on 2022-01-18 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0011_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='comment',
            new_name='replied_to',
        ),
    ]
