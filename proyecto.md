# Proyecto: LibroLibre

## Descripción General

LibroLibre es una aplicación web diseñada para estudiantes universitarios. Su objetivo es facilitar el intercambio, préstamo o donación de libros entre alumnos de la misma institución.

Los estudiantes podrán publicar libros que ya utilizaron en semestres anteriores y que desean regalar o prestar a otros compañeros, fomentando el apoyo académico y el aprovechamiento de recursos.

---

# MÓDULO 1: ANÁLISIS Y DISEÑO

## Funcionamiento General

El sistema permite que los estudiantes consulten libros disponibles, publiquen nuevos libros y contacten a otros estudiantes para solicitar ejemplares.

### Happy Path (Camino Feliz)

1. Un estudiante accede al sistema.
2. Visualiza el catálogo de libros disponibles.
3. Encuentra un libro de interés, por ejemplo "Cálculo Diferencial".
4. Selecciona la opción "Solicitar".
5. El sistema muestra la información de contacto del propietario del libro.
6. Ambos estudiantes se comunican para acordar el préstamo o la entrega.

### Unhappy Path (Camino Triste)

1. Un estudiante intenta solicitar un libro.

2. El sistema verifica la disponibilidad.

3. Detecta que otro estudiante ya realizó la solicitud previamente.

4. Se muestra el mensaje:

   "Este libro ya no está disponible."

5. La solicitud es cancelada sin afectar la navegación del usuario.

### Alternative Path (Camino Alternativo)

1. Un estudiante accede al sistema.
2. Decide publicar un libro en lugar de solicitar uno.
3. Completa un formulario sencillo.
4. Ingresa el título del libro.
5. Adjunta una fotografía.
6. Publica el libro para que otros estudiantes puedan visualizarlo.

---

# MÓDULO 2: BASE DE DATOS

La base de datos estará compuesta únicamente por dos tablas principales.

## Tabla: Usuarios

Almacena la información de los estudiantes registrados.

### Campos

* id
* nombre
* correo_institucional
* contraseña

## Tabla: Libros

Almacena los libros publicados por los estudiantes.

### Campos

* id
* titulo
* autor
* estado
* foto
* usuario_id

### Relación

* Un usuario puede publicar múltiples libros.
* Un libro pertenece a un único usuario.

### Restricción de Base de Datos

El campo `titulo` debe tener la restricción `NOT NULL`.

### Justificación

No tiene lógica de negocio permitir que un estudiante publique un libro sin nombre. El sistema requiere un título para identificarlo y mostrarlo correctamente en el catálogo.

---

# MÓDULO 3: IMPLEMENTACIÓN CON DJANGO

El sistema será desarrollado utilizando Python y Django.

## Autenticación

Se aprovechará el sistema de autenticación integrado de Django para:

* Registro de usuarios.
* Inicio de sesión.
* Gestión de sesiones.
* Protección de vistas privadas.

## Pantalla Principal

La página principal mostrará un catálogo de libros mediante tarjetas (cards) con:

* Imagen del libro.
* Título.
* Autor.
* Estado.
* Botón para solicitar.

## Publicación de Libros

Los usuarios podrán registrar nuevos libros mediante un formulario sencillo.

## Perfil del Estudiante

Cada usuario podrá visualizar los libros que ha publicado dentro del sistema.

---

# DESPLIEGUE

## Base de Datos

Se utilizará Supabase como servicio de base de datos en la nube.

## Hosting

La aplicación Django será desplegada en Render.

## Resultado Esperado

El sistema contará con una URL pública accesible para que los docentes puedan evaluarlo desde cualquier lugar.

---

# VENTAJAS DEL PROYECTO

## Simplicidad

* Solo dos tablas principales.
* Lógica de negocio sencilla.
* Fácil mantenimiento.

## Sin Pasarelas de Pago

Al tratarse de préstamos o donaciones entre estudiantes, no se requiere implementar pagos electrónicos ni simuladores de compra.

## Pocas Pantallas

El sistema requiere únicamente:

1. Inicio de sesión.
2. Catálogo de libros.
3. Formulario para publicar libros.
4. Perfil del estudiante.

## Valor Académico

El proyecto permite demostrar:

* Modelado de bases de datos.
* Relaciones entre tablas.
* Autenticación de usuarios.
* Formularios.
* CRUD básico.
* Despliegue en la nube con Django.
