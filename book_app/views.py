from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.db.models import Avg, Max, Min
from .models import BOOK
# Create your views here.



def index(request):
    books = BOOK.objects.all().order_by('-rating')
    num_books = books.count()
    avg_book_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_app/index.html',{'books':books, 'avg_books':avg_book_rating, 'num_books':num_books})



def book_detail(request, slug):
    # try:
    #     book = BOOK.objects.get(pk=id)
    # except Exception:
    #     raise Http404()

    book = get_object_or_404(BOOK, slug=slug)
    context ={
        'title' : book.title,
        'rating': book.rating,
        'author' : book.author,
        'is_bestselling' :book.is_bestselling,
        }
    return render(request, 'book_app/book_detail.html',context)