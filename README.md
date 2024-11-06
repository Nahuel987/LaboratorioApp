# Proyecto de Gestión de Laboratorios

Este proyecto es una aplicación de Django para gestionar laboratorios, directores generales y productos. Permite realizar operaciones CRUD y consultas sobre estos modelos.

## Requisitos

- Python 3.x
- Django
- PostgreSQL (u otra base de datos compatible)

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. **Crea y activa un entorno virtual**:
   ```bash
  python -m venv entorno
  source entorno/bin/activate

3. **Instala las dependencias**:
   ```bash
  pip install -r requirements.txt

4. **Configura la base de datoss**:
   ```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario_db',
        'PASSWORD': 'contraseña_db',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. **Aplica las migraciones:**:
   ```bash
  python manage.py migrate

6. **Crea un superusuario:**:
   ```bash
  python manage.py createsuperuser

## Instalación

1. **Ejecuta el servidor de desarrollo**:
   ```bash
   python manage.py runserver

2. **Accede al panel de administración**:
   ```bash
   URL: http://127.0.0.1:8000/admin
   Usa las credenciales del superusuario que creaste anteriormente.

## Estructura de las URLs

1. **Ingresar**:
   ```bash
   http://127.0.0.1:8000/laboratorio/ingresar/
   Con esta url puedes ingresar un nuevo laboratorio

2. **Ver listado de laboratorios**:
   ```bash
   http://127.0.0.1:8000/laboratorio/mostrar/
   Con esta url puedes ver los laboratorios ingresados, ademas desde alli puedes actualizarlos o eliminarlos
   
