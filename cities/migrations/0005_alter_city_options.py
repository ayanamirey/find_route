# Generated by Django 4.0.4 on 2022-04-18 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_alter_city_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
    ]
