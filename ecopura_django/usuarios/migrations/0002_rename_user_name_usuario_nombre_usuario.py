# Generated by Django 4.0.6 on 2022-11-16 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='user_name',
            new_name='nombre_usuario',
        ),
    ]
