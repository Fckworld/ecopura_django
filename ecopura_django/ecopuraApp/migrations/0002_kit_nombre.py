# Generated by Django 4.1 on 2022-09-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecopuraApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kit',
            name='nombre',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
