# Generated by Django 5.1.6 on 2025-02-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('access', models.CharField(choices=[('any', 'Anyone'), ('email_required', 'Email required')], default='email_required', max_length=14)),
                ('status', models.CharField(choices=[('publish', 'Published'), ('soon', 'coming soon'), ('draft', 'Draft')], default='draft', max_length=14)),
            ],
        ),
    ]
