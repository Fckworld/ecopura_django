# Generated by Django 4.0.6 on 2022-11-22 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_groups_usuario_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='is_staff',
        ),
    ]
