# Generated by Django 4.0.1 on 2022-01-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_video_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
