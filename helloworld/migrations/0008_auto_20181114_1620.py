# Generated by Django 2.1.2 on 2018-11-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0007_tarjetacredito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjetacredito',
            name='numero_tarjeta',
            field=models.CharField(max_length=30),
        ),
    ]