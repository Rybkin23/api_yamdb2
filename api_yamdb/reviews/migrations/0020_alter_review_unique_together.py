# Generated by Django 3.2 on 2023-07-11 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0019_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('author', 'title')},
        ),
    ]
