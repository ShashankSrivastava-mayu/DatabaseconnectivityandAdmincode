from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
    book= Book.objects.all()
    book_count=book.count()
    return render(request,"Books/index.html",
           {
               "books": book,
               "book_counts": book_count
           }     
    )
    
def book_next(request, slug):#used slug inplace of id which we have defined in models.py
    book = Book.objects.get(slug=slug)#pk means primary key
    return render(request,"Books/store_book.html",
        {
            "title":book.Title,
            "Book_Count":book.Book_Count,
            "author":book.author
        }
    )
