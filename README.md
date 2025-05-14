# Mi Portfolio en Django

Este es un proyecto personal desarrollado con **Django**, donde muestro mis habilidades y conocimientos en el desarrollo web. A través de este portfolio, puedes explorar las diferentes aplicaciones que he creado, cada una con su propósito único, para demostrar mi versatilidad como desarrolladora.

## Aplicaciones incluidas:

### Descripción de las aplicaciones en el proyecto:

- **Core**: La aplicación base que maneja elementos fundamentales y la estructura general del proyecto, proporcionando configuraciones comunes y recursos compartidos.

- **Blog**: 
  - Esta aplicación gestiona la visualización de entradas de blog. Define modelos que almacenan información sobre cada publicación, como el título, contenido, fecha de publicación, etc.
  - También se encarga de las vistas y plantillas para mostrar las entradas de forma ordenada y atractiva.

- **Social**: 
  - Esta app facilita la integración de los **iconos de redes sociales**, permitiendo que los usuarios puedan interactuar con plataformas externas (Facebook, Twitter, LinkedIn, etc.) a través de enlaces en el sitio web.
  
- **Contact**: 
  - Maneja la funcionalidad del formulario de contacto. Permite a los visitantes enviar mensajes desde el sitio web, almacenando los datos de contacto y notificando a los administradores sobre nuevos mensajes a través de notificaciones o correos electrónicos.

- **Proyectos**: 
  - Contiene un modelo para almacenar información sobre los proyectos en los que has trabajado o estás trabajando. Los modelos incluyen campos como **título**, **descripción**, **fecha de creación** y cualquier otra información relevante que desees mostrar sobre los proyectos.
  - También se encarga de mostrar esta información en el sitio web, permitiendo a los usuarios ver tus trabajos anteriores de manera organizada.

- **Curriculum**: 
  - Esta app se utiliza para **mostrar tu currículum** o **CV** en línea. Presenta **entradas** con **texto**, **fotos**, **títulos** y enlaces hacia tu **currículum en PDF**, **GitHub**, **LinkedIn** y otras plataformas relevantes.
  - La app permite estructurar y organizar tu información profesional de manera atractiva, incluyendo tu experiencia laboral, formación académica, habilidades y logros, todo con enlaces directos a tus perfiles y trabajos destacados.


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
