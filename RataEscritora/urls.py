"""
URL configuration for RataEscritora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pagina.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Vista de admin
    path('admin/', admin.site.urls),

    # Vistas generales
    path('', index, name='inicio'),
    path('historias/', historias, name='historias'),
    path('podcast/', podcast, name='podcast'),
    path('blog/', blog, name='blog'),
    path('sobre-mi/', sobre_mi, name='sobre-mi'),

    # Inicio de sesión y registro de usuario
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', exit, name='exit'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Vistas de perfil de usuario
    path('perfil/', perfil_usuario, name='perfil_usuario')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)