# Generated by Django 4.0.4 on 2022-06-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_listing_highest_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='highest_bid',
            new_name='curren_price',
        ),
        migrations.AlterField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
