# Generated by Django 3.2 on 2023-07-11 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0017_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('author', 'title')},
        ),
    ]
