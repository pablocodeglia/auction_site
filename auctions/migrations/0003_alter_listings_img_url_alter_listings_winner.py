# Generated by Django 4.0.4 on 2022-06-15 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listings_comments_biddings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='img_url',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='listings',
            name='winner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='winner_of_listing', to=settings.AUTH_USER_MODEL),
        ),
    ]
