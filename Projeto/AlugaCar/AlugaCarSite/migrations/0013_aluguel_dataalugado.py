# Generated by Django 2.2.3 on 2019-07-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlugaCarSite', '0012_auto_20190707_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='dataAlugado',
            field=models.DateField(null=True),
        ),
    ]
