# Generated by Django 3.0.2 on 2020-01-03 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fabricante', models.CharField(max_length=50)),
                ('codigoBarras', models.CharField(max_length=20)),
                ('unidad', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('creado', models.DateField(auto_now_add=True)),
                ('enUso', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Estante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('creado', models.DateField(auto_now_add=True)),
                ('enUso', models.BooleanField()),
                ('refUbicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantry.Ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('caducidad', models.DateField()),
                ('refEstante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantry.Estante')),
                ('refReferencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantry.Referencia')),
            ],
        ),
    ]
