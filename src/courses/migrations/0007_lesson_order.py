# Generated by Django 5.1.6 on 2025-02-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_lesson_thumbnail_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='order',
            field=models.BigIntegerField(default=0),
        ),
    ]
