# Generated by Django 5.1.7 on 2025-03-26 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Scraper', '0002_alter_scrape_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scrape',
            new_name='Link',
        ),
    ]
