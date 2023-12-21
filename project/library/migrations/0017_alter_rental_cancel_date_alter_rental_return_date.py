# Generated by Django 4.2.5 on 2023-12-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_rental_cancel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='cancel_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='予約取消日'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='返却手続日'),
        ),
    ]
