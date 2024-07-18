from django.contrib import admin
from django.urls import path, include
from kangacook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('kangacook.urls')),
    path('', views.home, name='home'), 
]
