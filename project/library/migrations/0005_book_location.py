# Generated by Django 4.2.5 on 2023-11-24 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_location_options_remove_book_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='library.location'),
        ),
    ]