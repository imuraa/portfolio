# Generated by Django 4.2.5 on 2024-01-18 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.PROTECT, to='library.category', verbose_name='カテゴリ'),
        ),
    ]