# Generated by Django 2.2.5 on 2019-11-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0011_imagen_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='ubicacion',
            field=models.CharField(max_length=255, null=True),
        ),
    ]