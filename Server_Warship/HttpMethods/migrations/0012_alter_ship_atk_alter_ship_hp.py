# Generated by Django 4.1.7 on 2023-02-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HttpMethods', '0011_alter_ship_atk_alter_ship_hp_alter_ship_board_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='Atk',
            field=models.IntegerField(default=11),
        ),
        migrations.AlterField(
            model_name='ship',
            name='Hp',
            field=models.IntegerField(default=67),
        ),
    ]