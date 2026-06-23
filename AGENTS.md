# AGENTS.md – Instrucciones rápidas para OpenCode

**¿Qué podría pasar desapercibido para un agente?**

- **Variable de entorno `DATABASE_URL`**
  - En `librolibre/settings.py` la base de datos se configura con:
    ```python
    import dj_database_url
    DATABASES = {"default": dj_database_url.config(default="sqlite:///db.sqlite3", conn_max_age=600)}
    ```
  - Si la variable `DATABASE_URL` no está definida, Django vuelve a SQLite (que no usamos en producción). **Por lo tanto, la variable debe estar presente y con el formato correcto** antes de lanzar la app.
  - Formato esperado por Render (PostgreSQL):
    `postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DBNAME>`
  - Cualquier carácter especial en la contraseña debe estar URL‑encoded (por ejemplo `@` → `%40`).

- **Pasos para configurar los entornos en Render**
  1. **Crear el servicio en Render**
     - Tipo: *Web Service*
     - Lenguaje: *Python*
     - Seleccionar el repositorio `will-dx/2-librolibre`.
  2. **En la sección *Environment* del servicio** agrega las siguientes variables:
     | Clave               | Valor (ejemplo)                                                | Comentario |
     |---------------------|----------------------------------------------------------------|------------|
     | `DJANGO_SECRET_KEY` | *(Render can generate a random value)*                         | Se usa para la firma de cookies y tokens. |
     | `DATABASE_URL`      | `postgres://myuser:myp%40ssword@aws-us-east-1-host:5432/librolibre` | Cadena de conexión que Render proporciona al crear la base de datos PostgreSQL. |
     | `DEBUG`             | `false`                                                       | En producción siempre `false`. |
     | `ALLOWED_HOSTS`     | `*` (o el dominio que Render asigna, e.g. `myapp.onrender.com`) | Permite que Django acepte peticiones al dominio de Render. |
  3. **Guardar los cambios** – Render iniciará automáticamente un *build*.
  4. **Verificar el build**
     - El `render.yaml` contiene los comandos exactos que Render ejecutará:
       ```yaml
       buildCommand: |
         pip install -r requirements.txt
         python manage.py collectstatic --noinput
         python manage.py migrate
       startCommand: gunicorn librolibre.wsgi:application
       ```
     - Estos pasos crean los archivos estáticos, aplican las migraciones (crean las tablas `books_usuario`, `books_libro`, `books_favorito`) y arrancan el servidor con Gunicorn.

- **Comandos de desarrollo locales que un agente debe saber**
  - Activar el entorno virtual:
    ```bash
    .venv\Scripts\activate   # Windows PowerShell
    # o source .venv/bin/activate   # en *nix
    ```
  - Instalar dependencias (si se añaden nuevas): `pip install -r requirements.txt`
  - Aplicar migraciones locales (útil para pruebas antes del push):
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
  - Ejecutar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```
  - Recoger archivos estáticos (solo en producción): `python manage.py collectstatic --noinput`

- **Gotchas específicos del proyecto**
  - **WhiteNoise** está habilitado en `MIDDLEWARE`; no es necesario configurar un servidor de archivos estáticos separado.
  - Las imágenes de los libros se guardan en `media/`; en Render deben permanecer persistentes mientras la instancia está activa.
  - El modelo `Usuario` es personalizado (`AUTH_USER_MODEL = 'books.Usuario'`). No crear usuarios con `createsuperuser` sin especificar este modelo.
  - El filtro de plantilla `is_favorited` está en `books/templatetags/favoritos.py`. Cargarlo con `{% load favoritos %}` donde se use.
  - El mapa de ubicación solo se renderiza si `latitud` y `longitud` están presentes; el botón *Obtener mi ubicación* usa la API del navegador y rellena esos campos.

---
**Resumen para el agente**
- ✅ Definir `DATABASE_URL` con el formato PostgreSQL antes de cualquier `runserver` o despliegue.
- ✅ Añadir las variables de entorno `DJANGO_SECRET_KEY`, `DEBUG=false` y `ALLOWED_HOSTS` en Render.
- ✅ El `render.yaml` ya contiene los comandos de build y start correctos.
- ✅ Usar los comandos locales indicados para desarrollo y pruebas.
- ✅ No olvidar crear la base de datos en Render y copiar la cadena de conexión exactamente (URL‑encode la contraseña).
