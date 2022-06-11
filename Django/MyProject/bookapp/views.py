from django.shortcuts import render
from django.contrib import messages
from . models import Book

############## ADD NEW BOOK ##############
def add_book(request):
    if 'add' in request.POST:
        a = int(request.POST['acc'])
        au = request.POST['author']
        tl = request.POST['title']
        Book(acc_no=a, title=tl, author=au).save(force_insert='__all__')
        messages.success(request, "Book with Ref ID " + str(a) + " is added succesfully...")
        return render(request, 'book_entry.html')
    else:
        return render(request, 'book_entry.html')

############## VIEW ALL BOOKS ##############
def view_book(request):
    results = Book.objects.all().order_by('acc_no')
    return render(request, 'view_all_books.html', {"Books" : results})

############## SEARCH SINGLE BOOK ##############
def search_book(request):
    if request.method == 'POST':
        tl = request.POST['title']
        current_book = Book.objects.get(title = tl)
        print(current_book.title)
        return render(request, 'search_book.html', {"cur_book" : current_book})
    else:
        return render(request, 'search_book.html')