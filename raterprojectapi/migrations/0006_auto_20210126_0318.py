# Generated by Django 3.1.3 on 2021-01-26 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raterprojectapi', '0005_auto_20210122_1742'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ratings',
            unique_together={('player', 'game')},
        ),
    ]
