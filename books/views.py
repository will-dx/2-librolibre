from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .models import Libro, Favorito
from .forms import RegisterForm, BookForm

# Registro customizado con confirmación de contraseña y toggle de vista
class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('books:list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# Lista de libros (catálogo)
class BookListView(ListView):
    model = Libro
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 12

# Detalle del libro
class BookDetailView(DetailView):
    model = Libro
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

# Crear libro (solo usuarios autenticados)
@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Libro
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

# Toggle favorito vía AJAX POST
@login_required
def toggle_favorite(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, libro=libro)
    if not created:
        favorito.delete()
        status = 'removed'
    else:
        status = 'added'
    return JsonResponse({'status': status})
