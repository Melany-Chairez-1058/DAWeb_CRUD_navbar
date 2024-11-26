# Generated by Django 5.1.2 on 2024-11-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_emp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Empleado')),
                ('puesto', models.CharField(max_length=50, verbose_name='Puesto ')),
                ('tel', models.CharField(max_length=11)),
                ('correo', models.EmailField(max_length=100, verbose_name='correo')),
                ('fecha_contrato', models.DateField(verbose_name='Fecha de contratacion')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salario')),
            ],
        ),
    ]
