# Generated by Django 3.2 on 2021-04-15 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default='untitled', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='preview_url',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default='untitled', max_length=100),
        ),
    ]
