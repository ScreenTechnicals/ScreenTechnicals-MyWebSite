# Generated by Django 4.0.1 on 2022-01-17 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('video_url', models.URLField()),
                ('overview', models.TextField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.playlist')),
            ],
        ),
    ]
