# Generated by Django 4.2.5 on 2024-01-12 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_alter_book_purchase_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image_url',
        ),
    ]
