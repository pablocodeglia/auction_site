# Generated by Django 4.0.4 on 2022-06-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_listing_highest_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='highest_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
