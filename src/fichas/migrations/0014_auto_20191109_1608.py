# Generated by Django 2.2.5 on 2019-11-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0013_auto_20191109_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='detalle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
