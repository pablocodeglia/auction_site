from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new_listing, name="new"),
    path("details/<int:id>/", views.listing_details_view, name="details"),
    path("watch/<int:id>/", views.watchlist_toggle, name="watchlist_toggle"),
    path("close/<int:id>/", views.close_listing_view, name='close'),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("won", views.won_view, name="won"),
    path("my_listings", views.my_items_view, name="my_listings"),
    path("categories", views.categories_view, name="categories"),
    path("categories/<str:cat>", views.category_view, name="category"),
]
