from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    """Usuario del sistema – usa los campos de AbstractUser.
    "correo_institucional" se mapea a ``email``.
    """
    # No extra fields needed; email will serve as institutional email.
    pass

class Libro(models.Model):
    titulo = models.CharField(max_length=255, blank=False, null=False)
    autor = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=50, default='disponible')
    foto = models.ImageField(upload_to='libros/', blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='libros')
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.autor})"

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='favoritos')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='favoritos')
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'libro')

    def __str__(self):
        return f"{self.usuario.username} ★ {self.libro.titulo}"