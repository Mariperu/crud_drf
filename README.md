# Django REST Framework

### Initial set up:

1. `py -m venv venv`
2. `source venv/scripts/activate`
3. `pip install django`
4. **`pip install djangorestframework`**
5. ` django-admin startproject crudproject .`
6. `py manage.py runserver`
7. `py manage.py startapp apps`
8. _setting.py_ :

   ```
   INSTALLED_APPS = [
    ...
    "rest_framework",
    "apps.apps.appsConfig",
   ]
   ```

9. `py manage.py runserver`
10. set up _apps/models.py_
11. set up any db ... _(by default: db.sqlite3)_
12. `py manage.py makemigrations apps`
13. `py manage.py migrate`

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

## Theory

### **Serializers**

Serializer refers to a process or a module that is responsible for converting complex data structures, such as objects or data collections, into a format that can be easily stored, transmitted, or reconstructed later.

Python provides several built-in modules for serialization, such as pickle, json, and yaml. These modules offer different serialization formats and methods to handle various data types.

---
