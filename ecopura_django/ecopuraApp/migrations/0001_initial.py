# Generated by Django 4.0.6 on 2022-11-21 03:22

from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('numero', models.IntegerField(null=True)),
                ('otro', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medio', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('numero', models.CharField(blank=True, max_length=30, null=True)),
                ('direccion', models.ManyToManyField(blank=True, null=True, to='ecopuraApp.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=300)),
                ('foto', models.ImageField(null=True, upload_to='')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.categoria')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nombre', models.CharField(max_length=100)),
                ('p_apellido', models.CharField(max_length=100)),
                ('empresa', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.IntegerField()),
                ('rut_empresa', models.CharField(blank=True, max_length=13, null=True)),
                ('rut_ver_empresa', models.CharField(blank=True, max_length=1, null=True)),
                ('correo', models.EmailField(max_length=254)),
                ('detalle_dispensador', models.CharField(choices=[('BS', 'Básico'), ('EL', 'Eléctrico'), ('AB', 'Ambos')], default='BS', max_length=2)),
                ('detalle_texto', models.TextField(null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nombre', models.CharField(max_length=100)),
                ('p_apellido', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=30, null=True)),
                ('empresa', models.CharField(blank=True, max_length=100, null=True)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.TextField(max_length=500)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nombre', models.CharField(max_length=100)),
                ('p_apellido', models.CharField(max_length=100)),
                ('s_apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('contrasenia', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_carro', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('producto', models.ManyToManyField(null=True, to='ecopuraApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impuesto', models.FloatField()),
                ('valor_total', models.IntegerField()),
                ('carrito', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.carrito')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.cliente')),
                ('pago', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecopuraApp.pago')),
            ],
        ),
    ]
