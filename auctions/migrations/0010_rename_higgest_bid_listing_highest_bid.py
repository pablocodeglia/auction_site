# Generated by Django 4.0.4 on 2022-06-16 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_listing_higgest_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='higgest_bid',
            new_name='highest_bid',
        ),
    ]
