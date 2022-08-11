# Generated by Django 4.0.4 on 2022-06-17 13:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_rename_curren_price_listing_current_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['-bid_timestamp']},
        ),
        migrations.AddField(
            model_name='listing',
            name='watchlists',
            field=models.ManyToManyField(blank=True, default=None, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]