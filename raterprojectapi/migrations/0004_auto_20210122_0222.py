# Generated by Django 3.1.3 on 2021-01-22 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raterprojectapi', '0003_auto_20201206_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='gamecat',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RemoveField(
            model_name='games',
            name='player_id',
        ),
    ]
