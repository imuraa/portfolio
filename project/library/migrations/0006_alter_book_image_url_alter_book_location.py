# Generated by Django 4.2.5 on 2023-11-27 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='画像リンク'),
        ),
        migrations.AlterField(
            model_name='book',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='library.location', verbose_name='保管場所'),
        ),
    ]