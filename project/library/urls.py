from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_book', views.search_book, name='search_book'),
    path('search_book/<int:num>', views.search_book, name='search_book'),
    path('book_detail/<int:num>', views.book_detail, name='book_detail'),
    path('set_period/<int:num>', views.set_period, name='set_period'),
    path('confirm_reservation/<int:num>', views.confirm_reservation, name='confirm_reservation'),
    path('reservation_completed/<int:num>', views.reservation_completed, name='reservation_completed'),
    path('return_book', views.return_book, name='return_book'),
    path('return_book/<int:num>', views.return_book, name='return_book'),
    path('confirm_return/<int:num>', views.confirm_return, name='confirm_return'),
    path('history', views.history, name='history'),
]