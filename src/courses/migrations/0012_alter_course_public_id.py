# Generated by Django 5.1.6 on 2025-03-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_lesson_options_lesson_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='public_id',
            field=models.CharField(blank=True, db_index=True, max_length=130, null=True),
        ),
    ]
