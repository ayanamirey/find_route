# Generated by Django 4.0.4 on 2022-04-18 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'qwer', 'verbose_name_plural': 'Города'},
        ),
    ]