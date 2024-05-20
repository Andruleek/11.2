from django.urls import path
from .views import authors_list, quotes_list, add_author, add_quote

urlpatterns = [
    path('authors/', authors_list, name='authors_list'),
    path('quotes/', quotes_list, name='quotes_list'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
]
