# Generated by Django 4.0.4 on 2022-06-17 14:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_bid_options_listing_watchlists'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='listing',
            managers=[
                ('custom_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
