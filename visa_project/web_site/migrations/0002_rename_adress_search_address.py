# Generated by Django 4.0.6 on 2022-11-12 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='adress',
            new_name='address',
        ),
    ]
