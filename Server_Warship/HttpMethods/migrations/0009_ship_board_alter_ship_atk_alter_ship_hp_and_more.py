# Generated by Django 4.1.7 on 2023-02-26 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HttpMethods', '0008_board_temp_status_alter_ship_atk_alter_ship_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='board',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='HttpMethods.board'),
        ),
        migrations.AlterField(
            model_name='ship',
            name='Atk',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='ship',
            name='Hp',
            field=models.IntegerField(default=67),
        ),
        migrations.AlterField(
            model_name='ship',
            name='owner',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='HttpMethods.player'),
        ),
    ]
