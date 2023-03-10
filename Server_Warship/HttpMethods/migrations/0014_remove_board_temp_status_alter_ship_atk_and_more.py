# Generated by Django 4.1.7 on 2023-02-26 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HttpMethods', '0013_alter_ship_atk_alter_ship_hp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='temp_status',
        ),
        migrations.AlterField(
            model_name='ship',
            name='Atk',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='ship',
            name='Hp',
            field=models.IntegerField(default=49),
        ),
        migrations.CreateModel(
            name='update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('front', models.IntegerField(default=1)),
                ('change', models.IntegerField(default=0)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HttpMethods.board')),
            ],
        ),
    ]
