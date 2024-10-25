# Generated by Django 5.1.2 on 2024-10-25 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=9)),
                ('titulo', models.CharField(max_length=50)),
                ('protagonista', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('resumen', models.CharField(max_length=2000)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('idGenero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPeliculas.generos')),
            ],
        ),
    ]
