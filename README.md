# Django REST Framework

## Theory

### **Serializers**

Serializer refers to a process or a module that is responsible for converting complex data structures, such as objects or data collections, into a format that can be easily stored, transmitted, or reconstructed later.

Python provides several built-in modules for serialization, such as pickle, json, and yaml. These modules offer different serialization formats and methods to handle various data types.

---

### Initial set up:

1. `py -m venv venv`
2. `source venv/scripts/activate`
3. `pip install django`
4. `python manage.py createsuperuser`
5. **`pip install djangorestframework`**
6. ` django-admin startproject crudproject .`
7. `py manage.py runserver`
8. `py manage.py startapp apps`
9. _setting.py_ :

   ```
   INSTALLED_APPS = [
    ...
    "rest_framework",
    "apps.apps.appsConfig",
   ]
   ```

10. Register _apps_ in _admin.py_.
11. `py manage.py runserver`
12. set up _apps/models.py_
13. set up any db ... _(by default: db.sqlite3)_
14. `py manage.py makemigrations apps`
15. `py manage.py migrate`

### **Rest API set up:**

GET/POST/UPDATE/PATCH

1. Inside apps folder create:

   - _serializers.py_ file.

   - _api.py_ file.

   Set up ...

2. Set up paths in _apps/urls.py_ file, using `routers` from _rest_framework_
3. **Include** apps paths in _project/urls.py_
4. `py manage.py runserver`

_**Note:**_: install _Thunder Client_ VSC extension (Ranga Vadhineni) to consult API in VSC directly, or use _Postman_ or others.

---

## Deploy in render

https://dashboard.render.com/

- Create New PostgreSQL
- Create New Web Service

### New PostgreSQL (for db)

- Name: nameDB
- Db: nameDB
- user: (EMPTY)
- Free
- Create db
- Go to dashboard

### New Web Service (for backend)

**Set up project:**

https://render.com/docs/deploy-django (since Update Your App For Render)

1.  Project, _setting.py_ :

    ```
    import os

    SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

    #Debug in dev = true / production=false
    DEBUG = 'RENDER' not in os.environ

    ALLOWED_HOSTS = []
    #Host in dev = [] / production=[url project]
    RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME: ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

    ```

2.  `pip install dj-database-url psycopg2-binary`

3.  Project, _setting.py_ :

    https://pypi.org/project/dj-database-url/ (View url schema)

    ```
     import dj_database_url

     DATABASES = {
         'default': dj_database_url.config(
             # PostgreSQL: default='postgresql://postgres:postgres@localhost:5432/mysite',
             #SQLite
             default= "sqlite:///db.sqlite3",
             conn_max_age=600
         )
    }
    ```

4.  Upload statics: `pip install whitenoise[brotli]`

    ```
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        ...
    ]
    ```

    ```
    STATIC_URL = '/static/'

        if not DEBUG:
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    ```

5.  _Create a Build Script_ (file to run scripts)

    - Create _build.sh_ file

      ```
          #!/usr/bin/env bash
          # exit on error
          set -o errexit

          pip install -r requirements.txt

          python manage.py collectstatic --no-input
          python manage.py migrate
      ```

    **Createsuperuser in Render** (Run only once):

    - Create environment variables in Render:

      CREATE_SUPERUSER = True
      DJANGO_SUPERUSER_EMAIL
      DJANGO_SUPERUSER_PASSWORD
      DJANGO_SUPERUSER_USERNAME

    - _build.sh_ file:

      ```
        ...
          if [[ $CREATE_SUPERUSER ]];
          then
          python manage.py createsuperuser --no-input
          fi
      ```

6.  Requirements: `pip freeze > requirements.txt`
7.  Allow buils.sh as executable: `chmod a+x build.sh`
8.  To serve content (as css, img, etc): `pip install gunicorn`

**Render**

9. Create a new Web Service
10. Connect a repository (choose a repository)
11. Connect
    - Name: name
    - Region: (choose)
    - Branch: main
    - Root Directory: (default)
    - Runtime: Python3
    - Build Command: _./build.sh_
    - Start command: gunicorn crudproject.wsgi
    - Free -> create _(it is going to fail because environment variables ...)_
12. Create environment variables:
    - From POSTGRESQL dashboard, copy the _Internal database URL_
    - Go to Web Service -> Environment
    - Key: DATABASE_URL -> Value: (paste copy)
    - Go to : https://randomkeygen.com/ , copy one Fort Knox Passwords
    - Key: SECRET_KEY -> Value: (paste psw)
    - Key:PYTHON_VERSION -> Value: 3.11.2
    - Save

**Verify Api REST** (Postman or tunder VSC)

https://drfcrud-test-kk2l.onrender.com/api/projects/

---

### django-import-export

1. `pip install django-import-export`
2. _settings.py_

   ```
   INSTALLED_APPS = (
           ...
           'import_export',
       )
   ```

3. `python manage.py collectstatic` (also verify to add **STATIC_ROOT** in settings.py )
4. Inside _apps/admin.py_, set up _django-import-export_

   ```
   from import_export import resources
   from import_export.admin import ImportExportModelAdmin
   ```

   - Create a resource class
   - Include: resource_class inside @admin class
