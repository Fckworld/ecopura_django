# Generated by Django 4.1 on 2022-09-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecopuraApp', '0008_alter_usuario_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.ManyToManyField(to='ecopuraApp.direccion'),
        ),
    ]