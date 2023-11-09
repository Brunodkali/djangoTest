# urls.py em menu app

from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_items, name='menu_items'),
    path('book_table/', views.book_table, name='book_table'),
]