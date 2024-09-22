django-admin startproject <your project name>
Go to the project directory
python manage.py makemigrations
python manage.py migrate
python manage.py startapp <your app name>
open settings.py to register the app:
In settings.py file look for "Installed_Apps" list,
and here include an element, 'your_app_name.apps.HomeConfig'
(Optional) If you want to host this project, add the domain name of the website in the "Allowed_Host" dictionary in settings.py
For eg.:- 'kumarprakhar.com' 

create two folders in your project directory : 
1. templates
2. static

Set these folders in settings.py:

i) STATICFILES_DIRS = [
    BASE_DIR / "static",
]
add this snippet at the end of settings.py
ii)
'DIRS': [BASE_DIR / "templates"]
add this snippet in the "templates" list in settings.py

Create index.html file in the templates folder
Go to urls.py:
import "include" library from django.urls

add this snippet in urlpatterns list:
 path('', include('home.urls'))

create a file "urls.py" in <your_app_name> directory
in this file write: 

from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
   path('', views.index, name='home'),
   #optional for eg.
   path('login', views.login, name='login'), 
   path('logout', views.logout, name='logout'),
]

define the functions for which path is defined in urls.py(index, login, logout for instance)
