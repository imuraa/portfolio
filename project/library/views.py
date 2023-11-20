from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

@login_required(login_url='/admin/login/')
def index(request):
    result  = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:9784773061437")
    data    = result.json()
    params = {
        'login_user':request.user,
        'title':data["items"][0]["volumeInfo"]["title"],
        'pub_date':data["items"][0]["volumeInfo"]["publishedDate"],
        'author':data["items"][0]["volumeInfo"]["authors"],
        'description':data["items"][0]["volumeInfo"]["description"],
        'thumbnail':data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"],
    }
    return render(request, 'library/index.html', params)
