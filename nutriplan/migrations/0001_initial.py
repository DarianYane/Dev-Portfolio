# Generated by Django 4.0.5 on 2023-01-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del alimento')),
                ('categoria', models.CharField(choices=[('opcion_1', 'Grasas'), ('opcion_2', 'Frutas'), ('opcion_3', 'Verduras'), ('opcion_4', 'Cereales y Legumbres'), ('opcion_5', 'Proteínas'), ('opcion_6', 'Lacteos'), ('opcion_7', 'Otros')], default='opcion_7', max_length=50)),
                ('calorias', models.IntegerField(verbose_name='Calorías por porción')),
                ('hidratos', models.IntegerField(verbose_name='Hidratos de Carbono por porción')),
                ('proteinas', models.IntegerField(verbose_name='Proteínas por porción')),
                ('grasas', models.IntegerField(verbose_name='Grasas por porción')),
                ('porcion', models.IntegerField(default=100, verbose_name='Tamaño de la porción')),
            ],
            options={
                'verbose_name': 'Alimento',
                'verbose_name_plural': 'Alimentos',
            },
        ),
    ]
