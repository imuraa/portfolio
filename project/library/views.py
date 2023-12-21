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
import datetime
from django.db.models import F


#マイページ
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
    rentals = Rental.objects.filter(book_id=num, cancel_date=None)
    reserved_dates = []
    js_reserved_dates = []
    #予約済みの日付を抽出
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
            #バリデーションOKの時
            request.session['form_data'] = request.POST
            return redirect('confirm_reservation', num=num)
            #return render(request, 'library/confirm_reservation.html', params)
        else:
            #バリデーションNGの時
            return render(request, 'library/set_period.html', params)
    else:
        #画面遷移（GET）した時
        form = RentalForm(request.session.get('form_data'))
        return render(request, 'library/set_period.html', params)
    

#貸出予約確認画面
@login_required(login_url='login')
def confirm_reservation(request, num):
    book = Book.objects.get(id=num)
    session_form_data = request.session.get('form_data')
    if session_form_data is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト
        return redirect('set_period', num=num)
    params = {
        'form': RentalForm(session_form_data),
        'book': book,
    }
    return render(request, 'library/confirm_reservation.html', params)


#貸出予約完了画面
@login_required(login_url='login')
def reservation_completed(request, num):
    book = Book.objects.get(id=num)
    session_form_data = request.session.pop('form_data', None)
    if session_form_data is None:
        return redirect('set_period', num=num)
    form = RentalForm(session_form_data)
    if form.is_valid():
        form.save()
        params = {
            'user_id':request.user,
            'book':book,
            'form':form,
        }
        return render(request, 'library/reservation_completed.html', params)
    


#書籍返却画面
@login_required(login_url='login')
def return_book(request, num=1):
    data = Rental.objects.filter(user_id=request.user, return_date=None)
    page = Paginator(data, 10)
    msg = '全' + str(data.count()) + '件'
    params = {
        'login_user':request.user,
        'data':page.get_page(num),
        'msg':msg,
    }
    return render(request, 'library/return_book.html', params)


#書籍返却確認画面
def confirm_return(request, num):
    today = datetime.datetime.today().date()
    if (request.method == "GET"):
        rental = Rental.objects.get(id=num)
        params = {
            'login_user':request.user,
            'rental':rental,
            'today':today,
        }
        return render(request, "library/confirm_return.html", params)
    else:
        rental = Rental.objects.get(id=num)
        #予約取消の場合
        if today < rental.start:
            rental.cancel_date = today
            rental.save()
        #返却の場合
        else: 
            rental.return_date = today
            rental.end = today
            rental.save()
        params = {
            'login_user':request.user,
            'rental':rental,
            'today':today,
        }
        return render(request, "library/return_completed.html", params)

#貸出返却履歴画面
@login_required(login_url='login')
def history(request):
    params = {
        'login_user':request.user,
    }
    return HttpResponse('ここは貸出返却履歴画面です')

