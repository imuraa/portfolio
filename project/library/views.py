from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import SearchForm, RentalForm
from .models import Book, Rental
from django.db.models import Q
from django.core.paginator import Paginator
import datetime
from django.shortcuts import redirect
from datetime import timedelta
import json



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
@login_required(login_url='login')
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


#貸出期間設定画面
@login_required(login_url='login')
def set_period(request, num):
    book = Book.objects.get(id=num)
    initial_dict = dict(book_id=num, user_id=request.user, start=None, end=None, return_date=None)
    rentals = Rental.objects.filter(book_id=num)
    reserved_dates = []
    js_reserved_dates = []
    for rental in rentals:
        start = rental.start
        end = rental.end
        days_num = (end - start).days + 1
        for i in range(days_num):
            reserved_dates.append(start + timedelta(days=i))
        for day in reserved_dates:
            js_reserved_dates.append(day.strftime('%Y/%m/%d'))
    params = {
            'login_user':request.user,
            'book':book,
            'form':RentalForm(initial=initial_dict),
            'js_reserved_dates':json.dumps(js_reserved_dates),
        }
    if (request.method == 'POST'):
        obj = Rental()
        form = RentalForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            form.save()
            return redirect(to='index')
        else:
            return render(request, 'library/set_period.html', params)
    else:
        return render(request, 'library/set_period.html', params)





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

