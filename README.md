# Proyecto de Gestión de Laboratorios

Este proyecto es una aplicación de Django para gestionar laboratorios, directores generales y productos. Permite realizar operaciones CRUD y consultas sobre estos modelos.

## Requisitos

- Python 3.x
- Django
- PostgreSQL 

## Instalación

1. **Clona el repositorio**:
  
  
2. **Crea y activa un entorno virtual**:
   ```bash
   python -m venv entorno
   source entorno/bin/activate  # En Windows: entorno\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**:
   En el archivo `settings.py`, ajusta la configuración de la base de datos:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'db_final_orm',
           'USER': 'userdjango',
           'PASSWORD': 'userdjango',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Aplica las migraciones**:
   ```bash
   python manage.py migrate
   ```

6. **Crea un superusuario**:
   ```bash
   python manage.py createsuperuser
   ```

## Uso

1. **Ejecuta el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

2. **Accede al panel de administración**:
   - URL: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   - Usa las credenciales del superusuario que creaste anteriormente.

## Estructura de las URLs del Administrador

1. **Ingresar un nuevo laboratorio**:
   - URL: [http://127.0.0.1:8000/laboratorio/ingresar/](http://127.0.0.1:8000/laboratorio/ingresar/)
   - Permite agregar un nuevo laboratorio.

2. **Ver listado de laboratorios**:
   - URL: [http://127.0.0.1:8000/laboratorio/mostrar/](http://127.0.0.1:8000/laboratorio/mostrar/)
   - Permite ver los laboratorios ingresados y desde allí actualizarlos o eliminarlos.
