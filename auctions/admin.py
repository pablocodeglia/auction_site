from django.contrib import admin
from .models import User, Listing, Bid, Comment, Category
# Register your models here.

admin.site.register(Listing),
admin.site.register(Bid),
admin.site.register(Comment),