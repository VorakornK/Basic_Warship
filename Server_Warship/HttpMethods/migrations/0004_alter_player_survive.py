# Generated by Django 4.1.7 on 2023-02-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HttpMethods', '0003_alter_player_front'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='survive',
            field=models.IntegerField(default=5),
        ),
    ]