# Generated by Django 3.2 on 2023-07-09 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20230709_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='description',
        ),
    ]