# Generated by Django 4.1 on 2022-12-18 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Institucion',
                'verbose_name_plural': 'Instituciones',
            },
        ),
        migrations.CreateModel(
            name='Inscritos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_inscripcion', models.DateField()),
                ('hora_inscripcion', models.TimeField()),
                ('estado', models.CharField(choices=[('Reservado', 'Reservado'), ('Completada', 'Completada'), ('Anulada', 'Anulada'), ('No Asisten', 'No Asisten')], default='No Asisten', max_length=20)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('institucion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crudApp.institucion')),
            ],
        ),
    ]
