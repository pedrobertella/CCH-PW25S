# Generated by Django 2.2.3 on 2019-07-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlugaCarSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='desricao',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='senha',
            field=models.CharField(max_length=50),
        ),
    ]