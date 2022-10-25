# Generated by Django 4.1.2 on 2022-10-24 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spotmusic', '0004_recentplayed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.AddField(
            model_name='song',
            name='language',
            field=models.CharField(choices=[('Spanish', 'Spanish'), ('English', 'English')], default='Spanish', max_length=20),
        ),
    ]
