# Generated by Django 4.1.7 on 2023-03-28 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborative', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
