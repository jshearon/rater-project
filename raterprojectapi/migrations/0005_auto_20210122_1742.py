# Generated by Django 3.1.3 on 2021-01-22 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raterprojectapi', '0004_auto_20210122_0222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameimages',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='gameimages',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='player_id',
            new_name='player',
        ),
    ]
