# Generated by Django 4.1.2 on 2022-10-26 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiProducto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagen_produc',
            new_name='imagen_produ',
        ),
    ]
