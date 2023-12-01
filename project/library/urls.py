from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_book', views.search_book, name='search_book'),
    path('search_book/<int:num>', views.search_book, name='search_book'),
    path('book_detail/<int:num>', views.book_detail, name='book_detail'),
    path('set_period/<int:num>', views.set_period, name='set_period'),
    path('return_book', views.return_book, name='return_book'),
    path('history', views.history, name='history'),
]