# Generated by Django 4.2 on 2025-01-15 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('E', 'Eléctrico'), ('A', 'Agua'), ('F', 'Fuego'), ('P', 'Planta'), ('L', 'Lagartija')], max_length=30),
        ),
    ]
