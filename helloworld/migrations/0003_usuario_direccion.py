# Generated by Django 2.1.2 on 2018-11-08 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_remove_usuario_tipo_casa'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
