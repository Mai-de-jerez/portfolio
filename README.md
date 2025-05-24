# Mi Portfolio en Django

Este es un proyecto personal desarrollado con **Django**, donde muestro mis habilidades y conocimientos en el desarrollo web. A través de este portfolio, puedes explorar las diferentes aplicaciones que he creado, cada una con su propósito único, para demostrar mi versatilidad como desarrolladora.

## Aplicaciones incluidas:

### Descripción de las aplicaciones en el proyecto:

- **Core**: es la aplicación base que maneja elementos fundamentales y la estructura general del proyecto, proporcionando configuraciones comunes y recursos compartidos.

- **Blog**: esta aplicación gestiona la visualización y administración de las entradas de blog. Incluye un conjunto completo de funcionalidades **CRUD** (Crear, Listar, Modificar, Eliminar) que permiten gestionar las publicaciones de manera eficiente. 

  - **Crear**: Permite a los usuarios crear nuevas publicaciones con información como el título, contenido, fecha de publicación, etc.
  - **Listar**: Muestra todas las entradas del blog de forma ordenada, generalmente con la opción de paginación.
  - **Modificar**: Permite editar y actualizar cualquier entrada existente del blog.
  - **Eliminar**: Ofrece la opción de eliminar publicaciones de forma sencilla.

La aplicación define modelos que almacenan la información sobre cada publicación y gestiona las vistas y plantillas para mostrar las entradas de manera ordenada y atractiva. Además, proporciona interfaces de administración para gestionar el contenido desde el backend.

- **Social**: Esta app facilita la integración de los **iconos de redes sociales**, permitiendo que los usuarios puedan interactuar con plataformas externas (Facebook, Twitter, LinkedIn, etc.) a través de enlaces en el sitio web.
 
- **Pages**: Esta aplicación está diseñada para manejar **páginas estáticas,** como el Aviso Legal, Política de Privacidad, Términos y Condiciones, etc. En lugar de crear cada una de estas páginas manualmente como vistas separadas, las agruparé dentro de una app que maneje las vistas y las URLs de estas páginas estáticas.
  
- **Contact**: Maneja la funcionalidad del formulario de contacto. Permite a los visitantes enviar mensajes desde el sitio web, almacenando los datos de contacto y notificando a los administradores sobre nuevos mensajes a través de notificaciones o correos electrónicos.

- **Proyectos**:  Contiene un modelo para almacenar información sobre los proyectos en los que he trabajado o estoy trabajando. Los modelos incluyen campos como: **título**, **descripción**, **fecha de creación**, y **enlace al proyecto**. También se encarga de mostrar esta información en el sitio web, permitiendo a los usuarios ver mis trabajos anteriores de manera organizada.

- **Curriculum**: Esta app se utiliza para **mostrar mi currículum** en línea. Presenta **entradas** con **texto**, **fotos**, **títulos** y enlaces hacia mi **currículum en PDF**, **GitHub**, **LinkedIn** y otras plataformas relevantes. La app permite estructurar y organizar mi información profesional de manera atractiva, incluyendo mi experiencia laboral, formación académica, habilidades y logros, todo con enlaces directos a mis perfiles y trabajos destacados.


## Características destacadas:
- Diseño limpio y moderno.
- Interactividad y facilidad de navegación.
- Utilización de las mejores prácticas en Django para el desarrollo web.

Este proyecto es una representación de mi evolución como desarrolladora, y está diseñado para ser escalable y fácil de mantener. Estoy emocionada de compartirlo contigo y espero que te guste.

---

## Instrucciones para clonar y ejecutar el proyecto

### Requisitos previos
Antes de comenzar, asegúrate de tener **Python 3.x** y **Django** instalados. También necesitarás **Git** para clonar el repositorio.

### Pasos para clonar y ejecutar el proyecto

1. **Clona el repositorio**:
   Para clonar este repositorio en tu máquina local, abre tu terminal o Git Bash y ejecuta el siguiente comando:

 ```bash
 git clone https://github.com/Mai-de-jerez/portfolio.git
 ```

2. **Accede al directorio del proyecto**:
  Después de clonar el repositorio, navega al directorio del proyecto con el siguiente comando:

```bash
cd portfolio
```

3. **Crea un entorno virtual (opcional pero recomendado)**:
  Es recomendable crear un entorno virtual para evitar conflictos con otras dependencias. Puedes crear un entorno virtual usando el siguiente comando:

```bash
python -m venv env
```

4. **Activa el entorno virtual**:
  Si estás en Windows, activa el entorno con:

```bash
.\env\Scripts\activate
```

  En Linux/macOS, usa:  
  
```bash
source env/bin/activate
```

5. **Instala las dependencias**:
  Una vez activado el entorno virtual, instala las dependencias del proyecto utilizando pip:

```bash
pip install -r requirements.txt
```

6. **Configura la base de datos**:
  Si es la primera vez que ejecutas el proyecto, necesitarás migrar las bases de datos. Ejecuta el siguiente comando:

```bash
python manage.py migrate
```

7. **Crea un superusuario (si deseas acceder al panel de administración de Django)**:
Para acceder al panel de administración de Django, necesitas crear un superusuario. Ejecuta el siguiente comando y sigue las instrucciones para crear el superusuario:

```bash
python manage.py createsuperuser
```

8. **Ejecuta el servidor**:
  Finalmente, puedes ejecutar el servidor de desarrollo con:

```bash
python manage.py runserver
```

Esto levantará el servidor en `http://127.0.0.1:8000/`. Puedes acceder a tu portfolio y también al panel de administración de Django en `http://127.0.0.1:8000/admin/` utilizando el superusuario que creaste.

## Autor
Este proyecto sí es mío 100%, y en él pude poner en práctica todo lo aprendido en el curso de ecperto en Django de Héctor Costa.
