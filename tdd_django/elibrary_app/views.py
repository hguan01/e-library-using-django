from django.shortcuts import render

from .forms import AddBookForm

def home(request):

    add_book_form = AddBookForm()

    return render(request, 'home.html', {
        "add_book_form": add_book_form,
    })