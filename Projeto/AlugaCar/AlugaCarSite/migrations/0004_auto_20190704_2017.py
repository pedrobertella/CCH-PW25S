# Generated by Django 2.2.3 on 2019-07-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlugaCarSite', '0003_auto_20190704_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
