# Generated by Django 4.1.2 on 2022-10-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiProducto', '0002_rename_imagen_produc_producto_imagen_produ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen_produ',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_produc',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
