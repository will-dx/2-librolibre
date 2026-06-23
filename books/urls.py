from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='list'),
    path('libro/<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    path('agregar/', views.BookCreateView.as_view(), name='add'),
    path('favorito/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),
]
