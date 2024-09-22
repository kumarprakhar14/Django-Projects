from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Prakhar Ice Creams"
admin.site.site_title = "Prakhar Ice Creams Admin"
admin.site.index_title = "Prakhar Ice Creams Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
