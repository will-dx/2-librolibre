from django import template

register = template.Library()

@register.filter
def is_favorited(book, user):
    """Devuelve True si el usuario tiene marcado el libro como favorito."""
    if not user.is_authenticated:
        return False
    return book.favoritos.filter(usuario=user).exists()
