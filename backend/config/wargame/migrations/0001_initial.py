# Generated by Django 5.0.3 on 2024-05-31 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wargame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_description', models.TextField()),
                ('quiz_flag', models.CharField(max_length=100)),
                ('quiz_title', models.CharField(max_length=100)),
                ('quiz_level', models.CharField(choices=[('high', 'High'), ('intermediate', 'Intermediate'), ('beginner', 'beginner')], max_length=20)),
                ('quiz_type', models.CharField(choices=[('web', 'Web'), ('system', 'System Hacking'), ('crypto', 'Crypto'), ('forensics', 'Forensics'), ('reversing', 'Reverse Engineering'), ('misc', 'Miscellaneous')], max_length=20)),
                ('quiz_file', models.FileField(blank=True, null=True, upload_to='wargame_files/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wargames', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
