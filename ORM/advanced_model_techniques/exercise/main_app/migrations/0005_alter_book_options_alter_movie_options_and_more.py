# Generated by Django 4.2.4 on 2023-11-26 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_book_movie_music'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Model Book', 'verbose_name_plural': 'Models of type - Book'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Model Movie', 'verbose_name_plural': 'Models of type - Movie'},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Model Music', 'verbose_name_plural': 'Models of type - Music'},
        ),
    ]
