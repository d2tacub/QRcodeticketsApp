from django.urls import path
from movies import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('book-ticket/', views.book_ticket, name='book_ticket'),
    path('ticket-confirmation/', views.ticket_confirmation, name='ticket_confirmation'),
]
