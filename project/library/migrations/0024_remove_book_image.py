# Generated by Django 4.2.5 on 2024-01-18 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0023_alter_book_category_alter_book_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]