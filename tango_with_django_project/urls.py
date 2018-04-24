from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from rango import views 

urlpatterns = [
    path('', views.index, name='index'), 
    path('rango/', include('rango.urls')), 
    path('admin/', admin.site.urls),
]
