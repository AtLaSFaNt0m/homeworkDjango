# Generated by Django 5.1.2 on 2024-11-05 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task4', '0002_buyer_game_delete_videogame'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('founded_year', models.IntegerField()),
                ('headquarters', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'developer',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'publisher',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='task4.developer'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='task4.publisher'),
        ),
    ]
