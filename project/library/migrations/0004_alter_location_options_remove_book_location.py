# Generated by Django 4.2.5 on 2023-11-24 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': '保管場所', 'verbose_name_plural': '保管場所'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='location',
        ),
    ]