# Generated by Django 4.1.7 on 2023-02-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HttpMethods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='num_player',
            field=models.IntegerField(default=0),
        ),
    ]