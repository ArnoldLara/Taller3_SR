# Generated by Django 2.2.3 on 2020-06-04 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_ratings_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='date',
        ),
    ]