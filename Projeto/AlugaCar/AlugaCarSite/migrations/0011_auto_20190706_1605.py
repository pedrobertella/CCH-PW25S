# Generated by Django 2.2.3 on 2019-07-06 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AlugaCarSite', '0010_auto_20190706_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlugaCarSite.Marca'),
        ),
        migrations.AlterField(
            model_name='carro',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlugaCarSite.Modelo'),
        ),
    ]