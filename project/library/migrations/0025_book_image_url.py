# Generated by Django 4.2.5 on 2024-01-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0024_remove_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.URLField(blank=True, verbose_name='画像URL'),
        ),
    ]
