from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    owner = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='owner_of_listing')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    init_price = models.DecimalField(max_digits=9, decimal_places=2)
    current_price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    img_url= models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey('User', null=True, blank=True, on_delete=models.DO_NOTHING, related_name='winner_of_listing')
    watchlists = models.ManyToManyField(User, related_name='watchlist', default=None, blank=True)

    class Meta:
        verbose_name_plural = 'Listings'
        ordering = ['creation_date']

    def save(self, *args, **kwargs):
        self.highest_bid = self.init_price
        super().save(*args, **kwargs)

    def __str__(self):
        if self.is_active == True:
            active_status = "ACTIVE"
        else:
            active_status = "CLOSED"

        return f"#{self.pk}: {self.title} [{active_status}]"
        

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Bid(models.Model):
    auction = models.ForeignKey('Listing', on_delete=models.DO_NOTHING)
    bidder = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    bid_timestamp = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-bid_timestamp']

    def __str__(self):

        return f'Bid for "{self.auction}" for ${self.amount} [by {self.bidder}]'


class Comment(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=300) 
    comment_timestamp = models.DateTimeField(auto_now_add = True)
    commenter = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-comment_timestamp']

    def __str__(self):

        return f'"{self.listing.title}" by user {self.commenter}' 