# from xml.etree.ElementTree import Comment
from django import forms
from django.forms import ModelForm
from auctions.models import Bid, Listing, Comment

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount', 'auction']
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'bidTextField'}),
        }

    def clean(self):
        bid = self.cleaned_data['amount']
        listing = self.cleaned_data['auction']

        if bid <= listing.current_price:
            print("Bid should be higher than current price")
            raise forms.ValidationError('Bid must be higher than current price')

class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'init_price', 'img_url', 'category']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }