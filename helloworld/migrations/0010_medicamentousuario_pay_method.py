# Generated by Django 2.1.2 on 2018-11-14 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0009_medicamentousuario_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamentousuario',
            name='pay_method',
            field=models.CharField(default='Efectivo', max_length=20),
        ),
    ]
