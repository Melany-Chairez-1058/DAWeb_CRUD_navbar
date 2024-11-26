# Generated by Django 5.1.2 on 2024-11-23 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=11)),
                ('direccion', models.CharField(max_length=100)),
                ('fecha', models.DateField(verbose_name='Fecha de Registro')),
            ],
        ),
    ]
