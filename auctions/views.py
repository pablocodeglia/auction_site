from typing_extensions import Required
from xml.etree.ElementTree import Comment
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import BidForm, CommentForm, NewListingForm
from .models import User, Listing, Bid, Comment, Category

def index(request):
    listings = Listing.objects.all()
    

    context = {
        'listings': listings
    }

    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='login')
def new_listing(request):
    if request.method == 'POST':
        form = NewListingForm(request.POST)
        print(form)
        if form.is_valid:
            form.instance.owner = request.user
            form.save()
    else:
        form = NewListingForm()
        return render(request, "auctions/new.html", {'form' : form })
    
    return redirect("index")


def listing_details_view(request, id):  
    # Get selected listing instance
    listing = Listing.objects.get(pk=id)
    # Check if listing is bookmarked
    if listing.watchlists.filter(id=request.user.id).exists():
        bookmark = True
    else:
        bookmark = False
    # Check if listing is active and, if closed, did you win?
    if listing.is_active:
        is_active = True
        won = False
    elif listing.winner == request.user:
        is_active = False
        won = True
    else:
        is_active = False
        won = False
    # Get comments from db
    comments = Comment.objects.filter(listing = listing)
    # Set-up Context
    context = {
    'listing': listing,
    'form' : BidForm(),
    'commentForm': CommentForm(),
    'id' : id,
    'bookmark' : bookmark,
    'is_active' : is_active,
    'won' : won,
    'comments' : comments,
    }

    if request.method == 'POST':
        if 'bid-button' in request.POST:
            form = BidForm(request.POST)
            if form.is_valid():
                form.instance.bidder = request.user
                form.save()
                listing.current_price = form.cleaned_data['amount']
                listing.save()
            else:
                context['form'] = form
                return render(request, "auctions/listing_details.html", context)
        if 'comment-button' in request.POST:
            commentForm = CommentForm(request.POST)
            if commentForm.is_valid():
                commentForm.instance.commenter = request.user
                commentForm.instance.listing = listing
                commentForm.save()
                print("ok!!")

    return render(request, "auctions/listing_details.html", context)


@login_required(login_url='login')
def watchlist_view(request):
    watchlist_items = Listing.objects.filter(watchlists=request.user)
    return render(request, 'auctions/watchlist.html', {'watchlist_items' : watchlist_items})


@login_required(login_url='login')
def won_view(request):
    won_items = Listing.objects.filter(winner=request.user)
    return render(request, 'auctions/won.html', {'won_items' : won_items})


@login_required(login_url='login')
def my_items_view(request):
    my_items = Listing.objects.filter(owner=request.user)
    return render(request, 'auctions/my_listings.html', {'my_items' : my_items})


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'auctions/category_list.html', {'categories' : categories})


def category_view(request, cat):
    category_items = Listing.objects.filter(Q(category__name=cat) & Q(is_active=True))
    return render(request, 'auctions/category_listings.html', {'category_items' : category_items, 'cat': cat})


@login_required(login_url='login')
def watchlist_toggle(request, id):
    listing = get_object_or_404(Listing, id=id)
    if listing.watchlists.filter(id=request.user.id).exists():
        listing.watchlists.remove(request.user)
        print("removed from watchlist")
    else:
        listing.watchlists.add(request.user)
        print("added to watchlist")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def close_listing_view(request, id):

    if request.method == 'POST':
        listing = get_object_or_404(Listing, id=id)
        # Get the winning bet so can retrieve the winner
        winning_bid = Bid.objects.get(Q(amount=listing.current_price) & Q(auction = listing))

        listing.is_active = False
        listing.winner = winning_bid.bidder
        listing.title = f"{listing.title} [CLOSED]"
        listing.save()
    
    return HttpResponseRedirect(reverse("index"))