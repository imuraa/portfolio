from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import SearchForm
from .models import Book, Rental
from django.db.models import Q
from django.core.paginator import Paginator
import datetime


@login_required(login_url='login')
def index(request):
    params = {
        'login_user':request.user,
    }
    return render(request, 'library/index.html', params)

#書籍検索画面
@login_required(login_url='login')
def search_book(request, num=1):
    
    if (request.method == "POST"):
        form = SearchForm(request.POST)
        search = request.POST["search"]
        data = Book.objects.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(publisher__icontains=search) |
            Q(isbn__iexact=search)
        )
        page = Paginator(data, 10)
        msg = '検索結果:' + str(data.count()) + '件'

    else:
        form = SearchForm()
        data = Book.objects.all()
        page = Paginator(data, 10)
        msg = ""

    params = {
        'login_user':request.user,
        'form':form,
        'data':page.get_page(num),
        'msg':msg,
    }
    return render(request, 'library/search_book.html', params)



#書籍詳細情報画面
def book_detail(request, num):
    book = Book.objects.get(id=num)
    today = datetime.datetime.today().date()
    data = Rental.objects.filter(book_id=num, start__lte=today, end__gte=today)
    if data.count():
        status = "貸出中"
    else:
        status = "貸出可"
    params = {
        'login_user':request.user,
        'book':book,
        'status':status,
    }
    return render(request, 'library/book_detail.html', params)




@login_required(login_url='login')
def return_book(request):
    params = {
        'login_user':request.user,
    }
    return HttpResponse('ここは書籍返却画面です')

@login_required(login_url='login')
def history(request):
    params = {
        'login_user':request.user,
    }
    return HttpResponse('ここは貸出返却履歴画面です')

