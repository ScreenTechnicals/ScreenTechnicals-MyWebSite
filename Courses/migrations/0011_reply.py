# Generated by Django 4.0.1 on 2022-01-18 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Courses', '0010_comment_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.video')),
            ],
        ),
    ]
