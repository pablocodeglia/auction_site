# Generated by Django 4.0.4 on 2022-06-16 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_bid_auction_listing_higgest_bid_alter_bid_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='higgest_bid',
            field=models.ForeignKey(blank=True, default=models.DecimalField(decimal_places=2, max_digits=9), null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
    ]
