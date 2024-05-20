from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AuthorForm, QuoteForm

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes_list')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

from django.shortcuts import render
from .models import Author, Quote

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'quotes/authors_list.html', {'authors': authors})

def quotes_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quotes_list.html', {'quotes': quotes})
